from django.shortcuts import render_to_response, redirect
from django.db import DatabaseError
from django.template import RequestContext
from MyPinterest.MyPinterestApp import User


def homepage(request):
    return render_to_response('../../User/templates/homepage.html', context_instance=RequestContext(request))

def userpage(request):
    return render_to_response('../../User/templates/homepage.html', context_instance=RequestContext(request))



def createUser(data):
    result={'result':False}
    try:
        user= User()
        user.name=data['username']
        user.email=data['email']
        user.set_password(data['pwd'])
        user.save()
        result['result']=True
    except DatabaseError:
        msg='database error. user not created'
        result['errmsg':msg]
    return result

def signup(request):
    if request.method=='GET':
        return render_to_response('../../User/templates/signup.html',context_instance=RequestContext(request))
    if request.method=='POST':
        postData=request.POST
        if createUser(postData)['result']:
            #redirect to user homepage, with session??
            return redirect('/userpage')

