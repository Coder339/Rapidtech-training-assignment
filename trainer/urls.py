from django.urls import path
from . import views


urlpatterns = [
    
    path('create/',views.TrainerCreateAPIView.as_view(),name = 'train-create'),
    path('list/',views.TrainerListAPIView.as_view(),name = 'train-list'),
    path('detail/<int:pk>/',views.TrainerDetailAPIView.as_view(),name = 'train-det'),

]