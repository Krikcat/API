import hashlib
import random
from django.shortcuts import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


# Create your views here.

@api_view(['POST'])
def register_api(request):
    if request.method == 'POST':
        serializer = user_s(data=request.data)
        Users = User.objects.filter(login=request.data["login"]).count()
        if Users == 0:
            if serializer.is_valid():
                serializer.save()
                return Response({"sucsefuly":True})
            return Response({"sucsefuly":False})
        else:
            return Response({"sucsefuly": False})
    else:
        return Response({"sucsefuly":False})

@api_view(['POST','DELETE'])
def login_api(request):
    user = User.objects.filter(login=request.data["login"]).filter(password=request.data["password"])
    if request.method == 'POST':
        if user.count() == 1:
            user = User.objects.get(login=request.data["login"])
            b = bytes(str(random.random()), encoding='utf-8')
            key = hashlib.sha1(b).hexdigest()
            user.key = key
            user.save()
            return Response({"sucsefuly":True,"key":key})
        else:
            return Response({"sucsefuly": False})
    elif request.method == 'DELETE':
        if user.count() == 1:
            user.delete()
            return Response({"sucsefuly": True})
        else:
            return Response({"sucsefuly": False}, status=404)
    else:
        return Response({"sucsefuly": False}, status=404)


@api_view(['POST','GET'])
def pet_api(request, key):
    k = User.objects.filter(key=key)
    if k.count() == 1:
        if request.method == 'GET':
            ser = pets_s(Pets.objects.all(), many=True)
            return Response(ser.data)
        elif request.method == 'POST':
            data = pets_s(data=request.data)
            if data.is_valid():
                data.save()
                return Response({"sucsefuly": True})
            else:
                return Response({"sucsefuly": False})
    else:
        return Response({"sucsefuly": False}, status=404)

@api_view(['PUT','DELETE'])
def pet_api2(request,key,pk):
    k = User.objects.filter(key=key).count()
    if k == 1:
        if request.method == 'DELETE':
            try:
                Pets.objects.get(id=pk).delete()
                return  Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})
        elif request.method == 'PUT':
            data = pets_s(Pets.objects.get(id=pk), data=request.data)
            if data.is_valid():
                data.save()
                return Response({"sucsefuly": True})
            else:
                return Response({"sucsefuly": False})
    else:
        Response({"sucsefuly": False}, status=404)

@api_view(['POST','GET','DELETE'])
def cage_api(request,key):
    k = User.objects.filter(key=key).count()
    if k == 1:
        if request.method == 'GET':
            ser = cage_s(Cage.objects.all(), many=True)
            return Response(ser.data)
        elif request.method == 'POST':
            Cage.objects.create().save()
            return Response({"sucsefuly": True})
        elif request.method == 'DELETE':
            try:
                Cage.objects.get(id=request.data["id"]).delete()
                return Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})
    else:
        Response({"sucsefuly": False}, status=404)

@api_view(['POST','DELETE'])
def cage_api2(request,key,pk):
    k = User.objects.filter(key=key).count()
    if k == 1:
        if request.method == 'POST':
            try:
                pets = Pets.objects.get(id=request.data["id"])
                cage = Cage.objects.get(id=pk)
                cage.pets_set.add(pets)
                cage.save()
                return Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})
        elif request.method == 'DELETE':
            try:
                Cage.objects.get(id=pk).pets_set.get(id=request.data["id"]).delete()
                return Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})
    else:
        Response({"sucsefuly": False}, status=404)

@api_view(['DELETE'])
def logout(request,key):
    k = User.objects.filter(key=key).count()
    if k == 1:
        if request.method == 'DELETE':
            k = User.objects.get(key=key)
            k.key = ''
            k.save()
            return Response({"sucsefuly": True})
    else:
        Response({"sucsefuly": False}, status=404)

@api_view(['POST','GET','DELETE'])
def bye_api(request,key):
    k = User.objects.filter(key=key).count()
    if k == 1:
        if request.method == 'GET':
            ser = bye_s(Bye.objects.all(), many=True)
            return Response(ser.data)
        elif request.method == 'POST':
            try:
                login = User.objects.get(key=key)
                price = 0
                pets = request.data["pets"]
                for i in pets:
                    p = Pets.objects.get(id=i).price
                    price += int(p)
                bye = Bye.objects.create(price=price, name=login.login)
                for i in pets:
                    bye.pets_set.add(Pets.objects.get(id=i))
                bye.save()
                return Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})

        elif request.method == 'DELETE':
            try:
                Bye.objects.get(id=request.data["id"]).delete()
                return Response({"sucsefuly": True})
            except:
                return Response({"sucsefuly": False})
    else:
        Response({"sucsefuly": False}, status=404)

