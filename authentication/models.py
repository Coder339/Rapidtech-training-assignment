from django.db import models
from django.contrib.auth.models import (AbstractUser)


position = (
    ('SUPER USER', 'super user'),
    ('USER', 'user')
)
class User(AbstractUser):
    role = models.CharField(verbose_name='user role', choices=position, 
                           max_length=20, default='unknown',null = True)

        
    class Meta:
        verbose_name_plural = 'user'
