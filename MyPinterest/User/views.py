import datetime
import logging
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.db import DatabaseError
from django.template import RequestContext
from django.contrib.auth import authenticate,logout
import django.contrib.auth as auth

from MyPinterest.Picture.models import Tag, Picture
from MyPinterest.Pinboard.models import Board , Pin
from MyPinterest.User.models import User
from MyPinterest.Relations.models import FollowStream, FriendStatus

@csrf_exempt
def verifyLogin(theUsername, thePassword, ip=None):
    result = {'result': False}
    print theUsername, thePassword
    user = authenticate(username=theUsername, password=thePassword)
    if user is not None:
        user.lastLoginTime = datetime.datetime.today()
        if ip is not None:
            user.lastLoginIP = ip
            user.save()
            result['result'] = True
        result['object'] = user
    else:
        logger = logging.getLogger("User")
        errorMsg = "Login error. User does not exist or incorrect password."
        logger.error(errorMsg)
        result['msg'] = errorMsg
    return result

@csrf_exempt
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return userpage(request)
        getData = request.GET
        if ('msg' in getData and len(getData['msg'])) > 0:
            return render_to_response('login.html', {"err_msg" : getData['msg']}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        request.session.clear()
        postData = request.POST
        if ('username' in postData and len(postData['username']) > 0
                and 'pwd' in postData and len(postData['pwd']) > 0):
            password = postData['pwd']
            ip = request.META['REMOTE_ADDR']
            loginResult = verifyLogin(postData['username'], password, ip)
            if loginResult['result']:
                user = loginResult['object']
                auth.login(request, user)
                return userpage(request)
            else:
                return render_to_response('login.html', {"errmsg" : "Incorrect Username/Password, please check!"}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', { "errmsg" : "Please input username"}, context_instance=RequestContext(request))

@csrf_exempt

def userpage(request):
        #get username from session
        user=request.user
        #get user's own boards
        boards=Board.objects.filter(owner=user)
        board_img = []
        for board in boards:
            pins = Pin.objects.filter(to_board=board)
            pl = list(pins)
            if pl:
                pin = pl[0]
                fimg = pin.picture
            else:
                fimg=  Picture.objects.get(id=12)
            item = dict()
            item['board'] = board
            item['img']=fimg
            board_img.append(item)
        #get user's follow streams
        streams = FollowStream.objects.filter(owner=user)
        friends = getFriends(user)
        data=dict()
        data['boards']=board_img
        data['Streams']= streams
        data['friends']=friends
        return render_to_response('userpage.html',data, context_instance=RequestContext(request))


@csrf_exempt
def createUser(data):
    result={'result':False}
    try:
        user= User.objects.create_user(name=data['username'],email=data['email'],createTime=datetime.datetime.now(),password=data['pwd'])
        user.save()
        result['result']=True
    except DatabaseError:
        msg='database error. user not created'
        result['errmsg']=msg
    return result

@csrf_exempt
def signup(request):
    if request.method=='GET':
        return render_to_response('signup.html',context_instance=RequestContext(request))
    if request.method=='POST':
        postData=request.POST
        createUserResult = createUser(postData)
        if createUserResult['result']:
            #redirect to user homepage, with session??
            request.session['user'] = request.POST['username']
            # return redirect('/userpage')
            return HttpResponseRedirect('/')
        else:
            return render_to_response('signup.html', {"errmsg" : "Sign up failed, username you choosed might be taken"}, context_instance=RequestContext(request))

@csrf_exempt
def userprofile(request):
    if request.method=="GET":
        req_user = request.user
        uid =request.GET['uid']
        visit_user = User.objects.get(id=uid)
        isSelf = req_user==visit_user
        boards = Board.objects.filter(owner=visit_user)
        res_boards = [board for board in boards if not (int(board.access_level)==0 or (int(board.access_level)==1 and req_user not in getFriends(visit_user)))]
        board_img = []
        for board in res_boards:
            pins = Pin.objects.filter(to_board=board)
            pl = list(pins)
            if pl:
                pin = pl[0]
                fimg = pin.picture
                item = dict()
                item['board'] = board
                item['img']=fimg
                board_img.append(item)
        friend_list = getFriends(visit_user)
        isFriend = request.user in friend_list
        requetedFriend = FriendStatus.objects.filter(from_user=request.user,to_user=visit_user,status=0)
        streams = FollowStream.objects.filter(owner=visit_user)
        data = dict()
        data['user']=visit_user
        data['isSelf']=isSelf
        data['boards']=board_img
        data['friends']=friend_list
        data['isFriend']=isFriend
        data['streams']=streams
        data['requested']=requetedFriend
        return render_to_response('userprofile.html',data, context_instance=RequestContext(request))

def getFriends(user):
    friend_relations = FriendStatus.objects.filter(from_user=user,status=1) | FriendStatus.objects.filter(to_user=user,status=1)
    friend_list = []
    for relation in friend_relations:
        friend = relation.from_user if relation.to_user==user else relation.to_user
        friend_list.append(friend)
    return friend_list

@csrf_exempt
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def changeemail(request):
    if request.method=="GET":
        return render_to_response('changeemail.html',context_instance=RequestContext(request))
    else:
        user = request.user
        new_email = request.POST['email']
        user.email=new_email
        user.save()
        return HttpResponseRedirect("/user/?uid="+str(user.id))
