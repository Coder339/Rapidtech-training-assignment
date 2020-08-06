from django.contrib import admin
from .models import Financials

# Register your models here.

class FinancialAdmin(admin.ModelAdmin):
    class Meta:
        model = Financials

    readonly_fields = ['tax']




admin.site.register(Financials,FinancialAdmin)

