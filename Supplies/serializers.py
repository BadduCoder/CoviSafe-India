from rest_framework import serializers

from .models import Supply
from Common.serializers import AddressSerializer


class SupplyListSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Supply
        fields = '__all__'
