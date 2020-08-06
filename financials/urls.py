from django.urls import path
from . import views


urlpatterns = [
    
    path('create/',views.FinancialCreateAPIView.as_view(),name = 'fin-create'),
    path('list/',views.FinancialListAPIView.as_view(),name = 'fin-list'),
    path('detail/<int:pk>/',views.FinancialDetailAPIView.as_view(),name = 'fin-det'),

]