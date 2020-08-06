from django.db import models
from django.db.models.signals import post_delete
from utils.validators import validate_phone_number
from authentication.models import User
# Create your models here.


status = (
    ('LEAD', 'Lead'),
    ('PROSPECT', 'Prospect'),
    ('IN TRAINING', 'In Training'),
    ('COMPLETED', 'Completed'),
    ('REJECTED', 'Rejected'),
    ('INVALID', 'Invalid'),
)



class TraineeInfo(models.Model):
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
    contact           = models.CharField(verbose_name='Consultant Phone',
                                         max_length=20,blank=False, null=True,validators=[validate_phone_number])
    email_id          = models.EmailField(verbose_name='Consultant Email',
                                          max_length=150, blank=False, null=True)
    t_s_d             = models.DateField(verbose_name='Training Start Date',editable=False,null=True)
    t_e_d             = models.DateField(verbose_name='Training End Date',editable=False,null=True)
    trainer           = models.CharField(max_length=50,blank=False,null=True,editable=False)
    status            = models.CharField(max_length=50,choices=status,blank=False,null=True)
    
    class Meta:
        verbose_name_plural = 'TraineeInfo'

    def save(self, *args, **kwargs):
        self.rate = round(self.rate, 2)
        print(self.pk)
        
        if not self.pk:    # new instance
            TraineeDash.objects.create(pk=self.pk,
                                    name=self.first_name + ' ' + self.last_name,
                                    contact=self.contact,
                                    email_id=self.email_id,
                                    technology=self.technology,
                                    status=self.status)
            item = TraineeDash.objects.get(name=self.first_name + ' ' + self.last_name)
            print(item.id)
        else:   # existing instance
            TraineeDash.objects.filter(pk=self.pk).update(
                                    name=self.first_name,
                                    contact=self.contact,
                                    email_id=self.email_id,
                                    technology=self.technology,
                                    status=self.status)

            
        super(TraineeInfo, self).save(*args, **kwargs)
        
        

    def __str__(self):
        return self.first_name + ' ' + self.last_name



def post_delete_dash(sender,instance,*args,**kwargs):
    name = instance.first_name + ' ' + instance.last_name
    TraineeDash.objects.filter(name=name).delete()                     # passing id not working as for now

post_delete.connect(post_delete_dash,sender=TraineeInfo)



# once the traineeinfo's instance is saved then traineedash will pull the information 

class TraineeDash(models.Model):
    trainee           = models.OneToOneField(TraineeInfo,on_delete=models.CASCADE,null=True,editable=False)
    name              = models.CharField(max_length=50,blank=True,null=True)
    contact           = models.CharField(verbose_name='Consultant Phone',
                                         max_length=20,blank=True, null=True)
    email_id          = models.EmailField(verbose_name='Consultant Email',
                                          max_length=150, blank=True, null=True)
    technology        = models.CharField(max_length=50,blank=True,null=True)
    status            = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'TraineeDash'



