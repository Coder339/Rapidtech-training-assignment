from rest_framework import serializers
from .models import Financials

class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Financials
        fields = ['id','trainee','bill_Rate','pay_Rate']
        read_only_fields = ['user']



        