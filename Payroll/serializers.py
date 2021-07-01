from rest_framework import serializers
from home.models import CreateContracts

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContracts
        fields = '__all__'
