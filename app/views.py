from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def schooljsondata(request):
    sod=School.objects.all()
    jod=SchoolModelSerializers(sod,many=True)
    jsondata=jod.data
    return Response(jsondata)