from rest_framework import serializers
from .models import LifePolicy

class LifePolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = LifePolicy
        fields = '__all__'