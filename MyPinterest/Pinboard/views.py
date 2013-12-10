from MyPinterest.Pinboard.models import Board
import datetime
from MyPinterest.User.models import User
from django.template.context import RequestContext

from django.shortcuts import render_to_response
from django.db import DatabaseError
from django.views.decorators.csrf import csrf_exempt
from MyPinterest.User.views import userpage
from MyPinterest.Pinboard.models import Pin

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
def boardpage(request):
    # we have user boardname
    # TODO: query for all pins in a board and return

    #implement add pin
    data = dict()
    try:
        bid = request.GET['b']
        board = Board.objects.get(id=bid)
        pins = Pin.objects.filter(to_board=board) #get all pins from a board
        pics = []
        for pin in pins:
            pics.append(pin.picture)
        data['board']=board
        data['pictures']=pics
    except DatabaseError:
        print "No data found"
    return render_to_response('boardpage.html',data,context_instance=RequestContext(request))