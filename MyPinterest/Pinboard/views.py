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

import StringIO
import PIL
from PIL import Image

# Create your views here.
@csrf_exempt
def createBoard(request):
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
        data['board']=board
        data['pictures']=pics
        data['user']=request.user #TODO should be other user object
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
        im = request.FILES['pic']
        picture=Picture.objects.create(first_piner=request.user,active=True,web_url='',image=im)
        print picture
        picture.save()
        bid = request.POST['board']
        board=Board.objects.get(id=bid)
        pin=Pin.objects.create(to_board=board,picture=picture,description=request.POST['description'])
        print pin
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
        data = dict()
        data['comments']=comments
        data['pin']=pin
        data['picture']=pin.picture
        data['board']=pin.to_board
        data['isOwner']=isOwner
        data['tags']=tags
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