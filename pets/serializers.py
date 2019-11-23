from rest_framework import serializers
from .models import User

class user_s( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['id','login','password']