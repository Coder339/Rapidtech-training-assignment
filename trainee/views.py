from django.shortcuts import render
from rest_framework.response import Response
from .models import TraineeInfo,TraineeDash
from .serializer import TraineeDashSerializer,TraineeInfoSerializer
from rest_framework import generics,permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class TraineeInfoCreateAPIView(generics.CreateAPIView):
    queryset                =       TraineeDash.objects.all()
    serializer_class        =       TraineeInfoSerializer
    permission_classes      =       [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes  =       [JSONWebTokenAuthentication,SessionAuthentication]

    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            response  =   {"message":"created","status":201}
            return Response(response,status=201)
        except:
            return Response({"message":"your form is invalid"})

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class TraineeInfoListAPIView(generics.ListAPIView):
    queryset                =       TraineeInfo.objects.all()
    serializer_class        =       TraineeInfoSerializer
    permission_classes      =       []
    authentication_classes  =       []



class TraineeInfoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =       TraineeInfo.objects.all()
    serializer_class        =       TraineeInfoSerializer
    permission_classes      =       [IsOwnerOrReadOnly]
    authentication_classes  =       [SessionAuthentication,JSONWebTokenAuthentication]
    lookup_field            =       'pk'




# Traineedash views

class TraineeDashCreateAPIView(generics.CreateAPIView):
    queryset                =       TraineeDash.objects.all()
    serializer_class        =       TraineeDashSerializer
    permission_classes      =       [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes  =       [JSONWebTokenAuthentication,SessionAuthentication]

    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            response  =   {"message":"created","status":201}
            return Response(response,status=201)
        except:
            return Response({"message":"your form is invalid"})

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class TraineeDashListAPIView(generics.ListAPIView):
    queryset                =       TraineeDash.objects.all()
    serializer_class        =       TraineeDashSerializer
    permission_classes      =       []
    authentication_classes  =       []



class TraineeDashDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =       TraineeDash.objects.all()
    serializer_class        =       TraineeDashSerializer
    permission_classes      =       [IsOwnerOrReadOnly]
    authentication_classes  =       [SessionAuthentication,JSONWebTokenAuthentication]
    lookup_field            =       'pk'
