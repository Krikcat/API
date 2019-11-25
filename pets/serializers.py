from rest_framework import serializers
from .models import *

class user_s( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['id','login','password']

class pets_s( serializers.ModelSerializer ):
    class Meta:
        model = Pets
        fields = ['id','name','sex','cage','bye','price']

class cage_s( serializers.ModelSerializer ):

    class Meta:
        model = Cage
        fields = ['id','pets_set']

class bye_s( serializers.ModelSerializer ):

    class Meta:
        model = Bye
        fields = ['id','name','pets_set','price']
