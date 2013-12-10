import datetime
import logging

from django.shortcuts import render_to_response, redirect
from django.db import DatabaseError
from django.template import RequestContext
from django.contrib.auth import authenticate
import django.contrib.auth as auth

from MyPinterest.Pinboard.models import Board
from MyPinterest.User.models import User
from MyPinterest.Relations.models import FollowStream


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

def login(request):
    if request.method == 'GET':
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


def userpage(request):
    #get username from session
    print 'User obj from session!:'
    print request.user.username
    user=request.user
    #get user's own boards
    boards=Board.objects.filter(owner=user)
    print boards
    #get user's follow streams
    streams = FollowStream.objects.filter(owner=user)
    context=dict()
    context['ownBoards']=boards
    context['Streams']= streams
    return render_to_response('userpage.html',context, context_instance=RequestContext(request))


def createUser(data):
    result={'result':False}
    try:
        print 'Got create password:'
        print data['pwd']
        user= User.objects.create_user(name=data['username'],email=data['email'],createTime=datetime.datetime.now(),password=data['pwd'])
        #user.set_password(data['pwd'])
        user.save()
        result['result']=True
    except DatabaseError:
        msg='database error. user not created'
        result['errmsg']=msg
    return result

def signup(request):
    if request.method=='GET':
        return render_to_response('signup.html',context_instance=RequestContext(request))
    if request.method=='POST':
        postData=request.POST
        createUserResult = createUser(postData)
        if createUserResult['result']:
            #redirect to user homepage, with session??
            request.session['user'] = request.POST['username']
            return redirect('/userpage')
        else:
            return render_to_response('signup.html', {"errmsg" : "Sign up failed, username you choosed might be taken"}, context_instance=RequestContext(request))