from MyPinterest.Pinboard.models import Board
import random
import datetime
from MyPinterest.User.models import User
from django.template.context import RequestContext

from django.shortcuts import render_to_response
from django.db import DatabaseError

# Create your views here.
def createBoard(request):
    result = {'result':True}
    try:
        username = request.user.username
        boardName = request.POST.get('boardname',''+username+'board'+random.randint(100,999))

        board = Board.objects.create()
        board.owner = request.user
        board.create_time = datetime.datetime.now()
        board.name = boardName

        board.save()
    except DatabaseError:
        result['result']=False
    return render_to_response('/userpage',context_instance=RequestContext(request))