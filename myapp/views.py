from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializers
from .models import UserInfo
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getalluser(request):
    if request.method=='GET':
        udata=UserInfo.objects.all()
        serial=UserSerializers(udata,many=True)
        return Response(serial.data)

@api_view(['GET'])
def getuser(request,id):
    try:
        uid=UserInfo.objects.get(id=id)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serail=UserSerializers(uid)
    return Response(serail.data)

@api_view(['POST'])
def saveuser(request):
    if request.method=='POST':
        serail=UserSerializers(data=request.data)
        if serail.is_valid():
            serail.save()
            return Response(data=serail.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateuser(request,id):
    try:
        uid=UserInfo.objects.get(id=id)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serial=UserSerializers(uid,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteuser(request,id):
    try:
        uid=UserInfo.objects.get(id=id)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        UserInfo.delete(uid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)




