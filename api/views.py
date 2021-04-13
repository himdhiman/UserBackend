from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models
from api import serializers
from django.db.models import F
import datetime

@api_view(['POST'])
def getData(request):
    if(request.POST['type'] == 'getdata'):
        data = request.POST['mail']
        qs = models.UserModel.objects.get(eMail = data)
        
        rank = 0
        for q in models.HistoryModel.objects.all().order_by('score')[::-1]:
            if q.id == qs.userDetail.pk:
                break
            rank += 1
        rank += 1
        qs.userDetail.rank = rank
        qs.userDetail.save()
        res = serializers.UserModelSerializer(qs)
        return Response(res.data)

    if(request.POST['type'] == 'createuser'):
        data = request.POST
        hm = models.HistoryModel(solved=0, partiallySolved=0, attemped=0, score=0, rank=0, problemsSolved="", problemPartiallySolved="")
        hm.save()
        um = models.UserModel(firstName=data['firstName'], lastName=data['lastName'], userName=data['userName'], eMail=data['mail'], passWord=data['passWord'], userDetail=hm)
        um.save()

    
    if(request.POST['type'] == 'update'):
        userIdentifier = request.POST['mail']
        qs = models.UserModel.objects.get(eMail = userIdentifier)
        if (request.POST['solved'] == "s"):
            qs.userDetail.solved = F('solved') + 1
            qs.userDetail.problemsSolved = qs.userDetail.problemsSolved + "-" + request.POST['probId']
        elif (request.POST['solved'] == "ps"):
            qs.userDetail.partiallySolved = F('partiallySolved') + 1
            qs.userDetail.problemPartiallySolved = qs.userDetail.problemPartiallySolved+ "-" + request.POST['probId']
        else:
            qs.userDetail.attemped = F('attemped') + 1
        dtm = models.DateTime(dateTime=datetime.datetime.now())
        dtm.save()
        qs.userDetail.dateTime.add(dtm)
        qs.userDetail.score = F('score') + request.POST['score']

        qs.userDetail.save()

        






    return Response("Hello")
