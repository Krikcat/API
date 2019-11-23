from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import user_s
from .models import User
# Create your views here.

@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = user_s(users,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = user_s(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"sucsefuly":True})
        return  Response({"sucsefuly":False})








