from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Requirement
from .serializers import RequirementSerializer
from Common.serializers import AddressSerializer


class RequirementListView(APIView):

    def get(self, request):
        requirements = Requirement.objects.filter(is_active=True)
        requirements_serialized = RequirementSerializer(requirements, many=True)
        return Response(requirements_serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        address_data = request.data.pop('address')
        address = AddressSerializer(data=address_data)
        if address.is_valid():
            address_instance = address.save()
        else:
            return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)

        requirement = RequirementSerializer(data=request.data)
        if requirement.is_valid():
            requirement_instance = requirement.save()
            requirement_instance.address = address_instance
            requirement_instance.save(update_fields=['address'])

            return Response(requirement.data, status=status.HTTP_201_CREATED)
        return Response(requirement.errors, status=status.HTTP_400_BAD_REQUEST)


class RequirementDetailView(APIView):

    def get(self, request, pk, format=None):
        try:
            requirement = Requirement.objects.get(pk=pk)
            requirement_serialized = RequirementSerializer(requirement)
            return Response(requirement_serialized.data, status=status.HTTP_200_OK)
        except Requirement.DoesNotExist:
            return Response("Requirement doesn't exists", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            requirement = Requirement.objects.get(pk=pk)
        except Requirement.DoesNotExist:
            return Response("Requirement doesn't exists", status=status.HTTP_404_NOT_FOUND)

        address_data = request.data.pop('address')
        existing_address = requirement.address
        address = AddressSerializer(existing_address, data=address_data, partial=True)
        if address.is_valid():
            address.save()
        else:
            return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)

        requirement_serialized = RequirementSerializer(requirement, data=request.data, partial=True)
        if requirement_serialized.is_valid():
            requirement_serialized.save()

            return Response(requirement_serialized.data, status=status.HTTP_201_CREATED)
        return Response(requirement_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            requirement = Requirement.objects.get(pk=pk)
            requirement.is_active = False
            requirement.save(update_fields=['is_active'])
            return Response("Requirement deleted successfully", status.HTTP_200_OK)
        except Requirement.DoesNotExist:
            return Response("Requirement doesn't exists", status=status.HTTP_404_NOT_FOUND)

