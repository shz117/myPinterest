from MyPinterest.Pinboard.models import Board
import datetime
from MyPinterest.User.models import User
from django.template.context import RequestContext

from django.shortcuts import render_to_response, HttpResponse
from django.db import DatabaseError
from django.views.decorators.csrf import csrf_exempt
from MyPinterest.User.views import userpage
from MyPinterest.Pinboard.models import Pin
from MyPinterest.Picture.models import Picture
from MyPinterest.Pinboard.models import Comment
from MyPinterest.Picture.models import Tag
from django.http import HttpResponseRedirect
from MyPinterest.Relations.models import FollowStream
import urllib2
from urlparse import urlparse
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from MyPinterest.User.views import getFriends

# Create your views here.
@csrf_exempt
def createBoard(request):
    if request.method=="GET":
        return render_to_response('createboard.html',context_instance=RequestContext(request))
    else:
        result = {'result':True}
        try:
            print request.user
            print request.POST
            boardName = request.POST.get('boardname')
            board = Board.objects.create(owner=request.user,create_time=datetime.datetime.now(),name=boardName,access_level=request.POST.get('access'))
            print board

            board.save()
        except DatabaseError:
            result['result']=False
        # return render_to_response('userpage.html',context_instance=RequestContext(request))
        return userpage(request)

@csrf_exempt
def boardpage(request,bid=None):
    #implement add pin
    data = dict()
    try:
        if not bid:
            bid = request.GET.get('b')
        board = Board.objects.get(id=bid)
        pins = Pin.objects.filter(to_board=board) #get all pins from a board
        pics = []
        for pin in pins:
            pin_pic = {}
            pin_pic['pin']=pin.id
            pin_pic['picture']=pin.picture
            pics.append(pin_pic)
        isOwner = board.owner==request.user

        #tell if user followed the board already
        streams = FollowStream.objects.filter(owner=request.user)
        boards = []
        for stream in streams:
            bs = stream.boards.all()
            for bd in bs:
                boards.append(bd)
        followed = board in boards

        data['board']=board
        data['pictures']=pics
        data['user']=request.user
        data['isOwner']=isOwner
        data['followed']=followed
    except DatabaseError:
        print "No data found"
    return render_to_response('boardpage.html',data,context_instance=RequestContext(request))

@csrf_exempt
def newpin(request):
    if request.method=='GET':
        data=dict()
        board=Board.objects.get(id=request.GET['b'])
        data['board']=board
        return render_to_response('newpin.html',data,context_instance=RequestContext(request))
    else:
        if len(request.FILES)!=0:
            im = request.FILES['pic']
            picture=Picture.objects.create(first_piner=request.user,active=True,web_url='',image=im)
            picture.save()
            bid = request.POST['board']
            board=Board.objects.get(id=bid)
            pin=Pin.objects.create(to_board=board,picture=picture,description=request.POST['description'])
            pin.save()
        else:
            #get image from url
            url = request.POST['pic_url']
            name = urlparse(url).path.split('/')[-1]
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urllib2.urlopen(url).read())
            img_temp.flush()
            picture=Picture.objects.create(first_piner=request.user,active=True,web_url='',image=File(img_temp))
            picture.save()
            bid = request.POST['board']
            board=Board.objects.get(id=bid)
            pin=Pin.objects.create(to_board=board,picture=picture,description=request.POST['description'])
            pin.save()
        request.method='GET'
        return boardpage(request,bid)

@csrf_exempt
def pinpage(request):
    if request.method=="POST" and request.POST.get('pid',None):
        #create comment
        pin = Pin.objects.get(id=request.POST['pid'])
        comment = Comment.objects.create(user=request.user,
                                         pin=pin,
                                         payload=request.POST['payload'],
                                         comment_time=datetime.datetime.now())
        comment.save()
        request.method='GET'
        return pinpage(request)
    elif request.POST.get('tag',None):
        tag = Tag.objects.create(name=request.POST['tag'])
        picture = Picture.objects.get(id=request.POST['picture'])
        picture.tags.add(tag)
        picture.save()
        return HttpResponseRedirect("/pin/?id="+str(request.POST['pin']))
    else:
        #render page
        pid = request.GET['id']
        pin = Pin.objects.get(id=pid)
        isOwner = pin.to_board.owner==request.user
        comments = Comment.objects.filter(pin=pin)
        tags = pin.picture.tags.all()
        # numbe of likes for this picture
        likes = len(pin.picture.liked_by_users.all())
        #tell if user already liked this picture
        liked = request.user in pin.picture.liked_by_users.all()
        data = dict()
        data['comments']=comments
        data['pin']=pin
        data['picture']=pin.picture
        data['board']=pin.to_board
        data['isOwner']=isOwner
        data['tags']=tags
        data['likes']=likes
        data['liked']=liked
        return render_to_response('pinpage.html',data,context_instance=RequestContext(request))

@csrf_exempt
def repin(request):
    if request.method=="GET":
        pin = Pin.objects.get(id=request.GET['pin'])
        boards = Board.objects.filter(owner=request.user)
        data = dict()
        data['pin']=pin
        data['boards']=boards
        return render_to_response('repinpage.html',data,context_instance=RequestContext(request))
    else:
        bid = request.POST['to_board']
        to_board = Board.objects.get(id=bid)
        picture = Picture.objects.get(id=request.POST['picture'])
        from_pin = Pin.objects.get(id=request.POST['from_pin'])
        pin = Pin.objects.create(to_board=to_board,picture=picture,from_pin=from_pin,
                                 description=request.POST['description'])
        pin.save()
        return HttpResponseRedirect("/pin/?id="+str(pin.id))

@csrf_exempt
def search(request):
    if request.method=="GET":
        return render_to_response('search.html',context_instance=RequestContext(request))
    else:
         #post search key words
        if request.POST.get('tag',None): #search by tag
            tagname = request.POST['tag']
            by = request.POST['by']
            tag_results = Tag.objects.filter(name__icontains=tagname)
            pics = Picture.objects.filter(tags__in=tag_results)
            pins = Pin.objects.filter(picture__in=pics)
            # convert queryset to python list
            pins = list(pins)
            # remove illegal pins, according to access level
            res_pins = [pin for pin in pins if not (int(pin.to_board.access_level) == 0 or (int(pin.to_board.access_level) == 1 and request.user not in getFriends(pin.to_board.owner)))]
            print res_pins
            # sort by time == sort by id
            if by=='time':
                pins.sort(key=lambda pin: pin.picture.id,reverse=True)
            else:
                # sort by likes
                pins.sort(key=lambda pin: len(pin.picture.liked_by_users.all()),reverse=True)
            data = dict()
            data['pins']=res_pins
            data['tag']=tagname
            data['by']=by
        elif request.POST.get('user',None):#search by user
            username = request.POST['user']
            users = User.objects.filter(username__icontains=username)
            data = dict()
            data['users']=users
            data['username']=username
        elif request.POST.get('stream',None): #search by stream
            stname = request.POST['stream']
            streams = FollowStream.objects.filter(name__icontains=stname)
            data = dict()
            data['streams']=streams
            data['stname']=stname
        else:
            data = dict()
        return render_to_response('searchresult.html',data,context_instance=RequestContext(request))

@csrf_exempt
def createStream(request):
    if request.method=="GET":
        return render_to_response('createstream.html',context_instance=RequestContext(request))
    else:
        result = {'result':True}
        try:
            print request.user
            print request.POST
            streamName = request.POST.get('streamname')
            stream = FollowStream.objects.create(owner=request.user,name=streamName)
            stream.save()
        except DatabaseError:
            result['result']=False
        # return render_to_response('userpage.html',context_instance=RequestContext(request))
        return userpage(request)

@csrf_exempt
def deletepin(request):
    pin = Pin.objects.get(id=request.GET['pin'])
    pic = pin.picture
    pin.delete()
    if pic.first_piner==request.user:
        pins = Pin.objects.filter(picture=pic)
        for p in pins:
            p.delete()
    return HttpResponseRedirect("/boardpage/?b="+str(request.GET['board']))

@csrf_exempt
def deleteboard(request):
    board = Board.objects.get(id=request.GET['bid'])
    pins = Pin.objects.filter(to_board=board)
    for pin in pins:
        pin.delete()
    board.delete()
    return HttpResponseRedirect("/")
