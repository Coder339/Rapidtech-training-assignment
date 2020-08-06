from django.shortcuts import render
from rest_framework.response import Response
from .models import Trainer
from .serializer import TrainerSerializer
from rest_framework import generics,permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class TrainerCreateAPIView(generics.CreateAPIView):
    queryset                =       Trainer.objects.all()
    serializer_class        =       TrainerSerializer
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



class TrainerListAPIView(generics.ListAPIView):
    queryset                =       Trainer.objects.all()
    serializer_class        =       TrainerSerializer
    permission_classes      =       []
    authentication_classes  =       []



class TrainerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =       Trainer.objects.all()
    serializer_class        =       TrainerSerializer
    permission_classes      =       [IsOwnerOrReadOnly]
    authentication_classes  =       [SessionAuthentication,JSONWebTokenAuthentication]
    lookup_field            =       'pk'