from django.shortcuts import render
from .models import LifePolicy
from .serializers import LifePolicySerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Policies(APIView):
    def get(self, request):
        policy_status = request.get('policy_status')
        customer_name = request.get('customer_name')
        created_date = request.get('created_date')
        if policy_status:
            all_policies = LifePolicy.objects.filter(policy_status=policy_status)
        if customer_name:
            all_policies = LifePolicy.objects.filter(customer_name=customer_name)
        if created_date:
            all_policies = LifePolicy.objects.filter(created=created_date)
        else:
            all_policies = LifePolicy.objects.all()
        serializer = LifePolicySerializer(all_policies, many=True)
        return Response(serializer.data)

