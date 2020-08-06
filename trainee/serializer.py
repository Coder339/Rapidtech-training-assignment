from rest_framework import serializers
from .models import TraineeDash,TraineeInfo

class TraineeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TraineeInfo
        fields = '__all__'
        read_only_fields = ['user']

class TraineeDashSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TraineeDash
        fields = '__all__'
        read_only_fields = ['user']