from django.db import models
from utils.validators import validate_phone_number
from authentication.models import User
# Create your models here.
class Trainer(models.Model):
    user              = models.ForeignKey(User,on_delete=models.CASCADE,null=True,editable=False)
    first_name        = models.CharField(max_length=50,blank=False,null=True)
    last_name         = models.CharField(max_length=50,blank=False,null=True)
    address_line1     = models.CharField(max_length=50,blank=False,null=True)
    address_line2     = models.CharField(max_length=50,blank=False,null=True,editable=False)
    city              = models.CharField(max_length=50,blank=False,null=True)
    state             = models.CharField(max_length=50,blank=False,null=True)
    country           = models.CharField(max_length=50,blank=False,null=True)
    zipcode           = models.IntegerField(blank=False,null=True)
    job_Title         = models.CharField(max_length=50,blank=False,null=True)
    technology        = models.CharField(max_length=50,blank=False,null=True)
    rate              = models.FloatField(blank=True,null=True)
    contact           = models.CharField(max_length=30,blank=False,null=True,
                                          validators=[validate_phone_number])
    email_id          = models.EmailField(verbose_name='Email',
                                          max_length=150, blank=False, null=True)
    
    class Meta:
        verbose_name_plural = 'Trainer'

    def save(self, *args, **kwargs):
        self.rate = round(self.rate, 2)
        super(Trainer, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name