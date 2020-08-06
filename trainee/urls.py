from django.urls import path
from . import views


urlpatterns = [
    
    path('info/create/',views.TraineeInfoCreateAPIView.as_view(),name = 'info-create'),
    path('info/detail/<int:pk>/',views.TraineeInfoDetailAPIView.as_view(),name = 'info-det'),
    path('info/list/',views.TraineeInfoListAPIView.as_view(),name = 'info-list'),

    path('dash/create/',views.TraineeDashCreateAPIView.as_view(),name = 'dash-create'),
    path('dash/detail/<int:pk>/',views.TraineeDashListAPIView.as_view(),name = 'dash-det'),
    path('dash/list/',views.TraineeDashDetailAPIView.as_view(),name = 'dash-list'),

]