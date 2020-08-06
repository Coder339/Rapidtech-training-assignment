from django.shortcuts import render
from rest_framework.response import Response
from .models import Financials
from .serializer import FinancialSerializer
from rest_framework import generics,permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from utils.permissions import IsOwnerOrReadOnly,IsSuper
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class FinancialCreateAPIView(generics.CreateAPIView):
    queryset                =       Financials.objects.all()
    serializer_class        =       FinancialSerializer
    permission_classes      =       [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes  =       [JSONWebTokenAuthentication,SessionAuthentication]

    def post(self,request,*args,**kwargs):
        try:
            self.create(request,*args,**kwargs)
            response  =   {"message":"created","status":201}
            return Response(response,status=201)
        except:
            return Response({"message":"your form is invalid or may be you are duplicating the data for existing financial"})

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class FinancialListAPIView(generics.ListAPIView):
    queryset                =       Financials.objects.all()
    serializer_class        =       FinancialSerializer
    permission_classes      =       []
    authentication_classes  =       []



class FinancialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                =       Financials.objects.all()
    serializer_class        =       FinancialSerializer
    permission_classes      =       [IsOwnerOrReadOnly]
    authentication_classes  =       [SessionAuthentication,JSONWebTokenAuthentication]
    lookup_field            =       'pk'