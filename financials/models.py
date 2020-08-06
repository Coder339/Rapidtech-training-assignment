from django.db import models
from django.db.models.signals import pre_save
from trainee.models import TraineeInfo
from authentication.models import User
# Create your models here.

class Financials(models.Model):
    user               = models.ForeignKey(User,on_delete=models.CASCADE,null=True,editable=False)
    trainee            = models.OneToOneField(TraineeInfo,
                                              on_delete=models.CASCADE,null=True)     # required bcoz we dont know 
                                                                                      # whose finacials we are storing of
    bill_Rate          = models.FloatField(blank=True,null=True)
    pay_Rate           = models.FloatField(blank=True,null=True)
    tax                = models.FloatField(blank=True,null=True)
    margin             = models.FloatField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name_plural = 'Financials'

    def save(self, *args, **kwargs):
        self.bill_Rate = round(self.bill_Rate, 2)
        self.pay_Rate  = round(self.pay_Rate, 2)
        super(Financials, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.trainee.first_name + ' ' + self.trainee.last_name

def pre_save_Margin(instance,sender,*args,**kwrags):
    
    instance.tax = instance.bill_Rate * (15/100)
    instance.margin = (instance.bill_Rate - (instance.pay_Rate  + instance.tax))

pre_save.connect(pre_save_Margin, sender=Financials)

