from MyPinterest.Pinboard.models import Board
import datetime
from MyPinterest.User.models import User
from django.template.context import RequestContext

from django.shortcuts import render_to_response, HttpResponse
from django.db import DatabaseError
from django.views.decorators.csrf import csrf_exempt
from MyPinterest.User.views import userprofile
from MyPinterest.Pinboard.models import Pin
from MyPinterest.Picture.models import Picture
from MyPinterest.Pinboard.models import Comment
from MyPinterest.Picture.models import Tag
from django.http import HttpResponseRedirect
from MyPinterest.Relations.models import FollowStream, FriendStatus

from MyPinterest.Pinboard.views import userpage

@csrf_exempt
def streampage(request):
    sid = request.GET['sid']
    stream = FollowStream.objects.get(id=sid)
    boards = stream.boards.all()
    board_img = []
    for board in boards:
        pins = Pin.objects.filter(to_board=board)
        pl = list(pins)
        if pl:
            pin = pl[0]
            fimg = pin.picture
            item = dict()
            item['board'] = board
            item['img']=fimg
            board_img.append(item)
    data = dict()
    isOwner = stream.owner==request.user
    data['boards']=board_img
    data['stream']=stream
    data['isOwner']=isOwner
    return render_to_response('streampage.html',data,context_instance=RequestContext(request))

@csrf_exempt
def followboard(request):
    if request.method=="GET":
        bid = request.GET['bid']
        board = Board.objects.get(id=bid)
        streams = FollowStream.objects.filter(owner=request.user)
        data = dict()
        data['board']=board
        data['streams']=streams
        return render_to_response('followboard.html',data,context_instance=RequestContext(request))
    else:
        stid = request.POST['to_stream']
        bid = request.POST['bid']
        board = Board.objects.get(id=bid)
        stream = FollowStream.objects.get(id=stid)
        stream.boards.add(board)
        stream.save()
        return userpage(request)

@csrf_exempt
def unfollowboard(request):
    if request.method=="GET":
        bid = request.GET['bid']
        board = Board.objects.get(id=bid)
        allstreams = FollowStream.objects.filter(owner=request.user)
        streams = []
        for stream in allstreams:
            if board in stream.boards.all():
                streams.append(stream)
        data = dict()
        data['streams']=streams
        data['board']=board
        return render_to_response('unfollowboard.html',data,context_instance=RequestContext(request))
    else:
        stid = request.POST['from_stream']
        bid = request.POST['bid']
        board = Board.objects.get(id=bid)
        stream = FollowStream.objects.get(id=stid)
        stream.boards.remove(board)
        stream.save()
        return userpage(request)

@csrf_exempt
def friendrequesthandler(request):
    to_uid = request.GET['to_uid']
    to_user = User.objects.get(id=to_uid)
    from_user = request.user
    _friend = FriendStatus.objects.filter(from_user=from_user,to_user=to_user)
    if not len(_friend)!=0:
        friend = FriendStatus.objects.create(from_user=from_user,to_user=to_user,status=0)
        friend.save()
    return HttpResponseRedirect("/user/?uid="+str(to_user.id))

@csrf_exempt
def viewfriendrequests(request):
    user = request.user
    requests = FriendStatus.objects.filter(to_user=user,status=0)
    data = dict()
    data['requests']=requests
    data['user'] = user
    return render_to_response('friendrequests.html',data,context_instance=RequestContext(request))

@csrf_exempt
def acceptrequest(request):
    from_user = User.objects.get(id=request.GET['from_user'])
    friend = FriendStatus.objects.get(from_user=from_user,to_user=request.user)
    friend.status=1
    friend.save()
    return HttpResponseRedirect("/friendrequests/?uid="+str(request.user.id))

@csrf_exempt
def rejecttrequest(request):
    from_user = User.objects.get(id=request.GET['from_user'])
    friend = FriendStatus.objects.get(from_user=from_user,to_user=request.user)
    friend.status=2
    friend.save()
    return HttpResponseRedirect("/friendrequests/?uid="+str(request.user.id))

@csrf_exempt
def like(request):
    user = request.user
    picture = Picture.objects.get(id=request.GET['pid'])
    picture.liked_by_users.add(user)
    picture.save()
    return HttpResponseRedirect("/pin/?id="+str(request.GET['pin']))

@csrf_exempt
def unlike(request):
    user = request.user
    picture = Picture.objects.get(id=request.GET['pid'])
    picture.liked_by_users.remove(user)
    picture.save()
    return HttpResponseRedirect("/pin/?id="+str(request.GET['pin']))

@csrf_exempt
def deletestream(request):
    stream = FollowStream.objects.get(id=request.GET['sid'])
    stream.delete()
    return HttpResponseRedirect("/")