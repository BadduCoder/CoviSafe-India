from rest_framework import serializers
from .models import Requirement

from Common.serializers import AddressSerializer


class RequirementSerializer(serializers.ModelSerializer):

    address = AddressSerializer(read_only=True)

    class Meta:
        model = Requirement
        fields = ['id',
                  'address',
                  'requirement_type',
                  'requirement_desc',
                  'primary_contact',
                  'secondary_contact',
                  'email',
                  'patient_name',
                  'fulfilled',
                  'quantity']

class RequirementDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = '__all__'
