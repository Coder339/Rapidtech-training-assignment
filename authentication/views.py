from django.shortcuts import render,redirect
from authentication.models import *
from .serializer import LoginSerializer
from rest_framework import permissions,authentication
from rest_framework import generics
from django.contrib.auth import authenticate,login
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    generics,
    status,
)
from .serializer import *
from . import views




class RegistrationView(generics.CreateAPIView):
    authentication_classes      =   []
    permission_classes          =   [] 
    serializer_class            =   RegisterSerializer
    # queryset                    =   User.objects.all()

    

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            serializer = RegisterSerializer(data = request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = RegisterSerializer.get_message(self,obj=user)
                data['email']    = user.email
                data['username'] = user.username
                data['token']    = RegisterSerializer.get_token(self,obj=user)  
            else:
                data = serializer.errors
            
            return Response(data)



# User=get_user_model()


class LoginAPIView(generics.GenericAPIView):
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   LoginSerializer
    # queryset                    =   User.objects.all()


    def post(self,request):
        username            =   request.data.get('username')
        password            =   request.data.get('password')
        user                =   authenticate(username=username,password=password)
        data = {}
        print(username)
        print(password)
        print(user)
        print(request.data)
        if user is not None:
            print('vvvv')
            login(request,user)
            serializer = LoginSerializer(data = request.data)
            data['response'] = LoginSerializer.get_message(self,obj=user)
            # response    =   {'messages':'you are logged in ...'}
            data['token']    = LoginSerializer.get_token(self,obj=user)
            # return Response(response)
            return Response(data)

        response    =   {'messages':'invalid credentials'}
        return Response(response)