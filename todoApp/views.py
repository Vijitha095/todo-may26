from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from todoApp.serializers import UserSerializer,TodoSerializer
from django.contrib.auth.models import User
from todoApp.models import Todo
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserRegisterView(CreateAPIView):
    serializer_class=UserSerializer

class TodoCreateListView(CreateAPIView,ListAPIView):
    serializer_class=TodoSerializer
    # authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

class TodoRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=TodoSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=Todo.objects.all()


class TodoCountView(APIView):
    def get(self,request):
        total_count=Todo.objects.filter(owner=request.user).count()
        pending_count=Todo.objects.filter(owner=request.user,status="pending").count()
        completed_count=Todo.objects.filter(owner=request.user,status="completed").count()
        return Response({"Total_count":total_count,"Pending_tasks":pending_count,"Completed_tasks":completed_count})



