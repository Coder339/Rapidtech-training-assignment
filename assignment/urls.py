from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('trainee/',include('trainee.urls')),
    path('trainer/',include('trainer.urls')),
    path('financial/',include('financials.urls')),
]
