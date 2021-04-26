from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Supply
from .serializers import SupplyListSerializer
from .constants import SupplyConstants
from Common.serializers import AddressSerializer


class SupplyListView(APIView):

    def get(self, request):
        # Fetch filters from url
        supply_type = self.request.query_params.get('r_type', None)
        supply_filter = SupplyConstants.R_TYPE_TO_SUPPLIES_MAPPING.get(supply_type, [])
        city = self.request.query_params.get('city', None)

        all_supplies = Supply.objects.filter(is_active=True)

        if supply_filter is not None:
            all_supplies = all_supplies.filter(supply_type__in=supply_filter)
        if city is not None:
            all_supplies = all_supplies.filter(address__city__icontains=city)

        supplies_data = SupplyListSerializer(all_supplies, many=True)
        return Response(supplies_data.data, status=status.HTTP_200_OK)
