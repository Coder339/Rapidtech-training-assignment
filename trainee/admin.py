from django.contrib import admin
from .models import TraineeInfo,TraineeDash
# Register your models here.

admin.site.register(TraineeInfo)



class TraineeDashAdmin(admin.ModelAdmin):
    class Meta:
        model = TraineeDash

    readonly_fields = ['name','contact','email_id','technology','status']


admin.site.register(TraineeDash,TraineeDashAdmin)


