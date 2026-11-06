from rest_framework import serializers
from django.contrib.auth.models import User
from todoApp.models import Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        read_only_fields=['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
        read_only_fields=['id','added_date','owner']
