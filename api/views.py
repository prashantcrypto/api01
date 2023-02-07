# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import generics

from .models import user_data
from .serializers import DataModelSerializer


class get_data(generics.ListAPIView):
    queryset = user_data.objects.all()
    serializer_class = DataModelSerializer


class post_data(generics.ListCreateAPIView):
    queryset = user_data.objects.all()
    serializer_class = DataModelSerializer


class walletDetail(generics.RetrieveAPIView):
    queryset = user_data.objects.all()
    serializer_class = DataModelSerializer
    lookup_field = 'wallet_address'


class TwitterLinkUpdate(generics.UpdateAPIView):
    queryset = user_data.objects.all()
    serializer_class = DataModelSerializer
    lookup_field = 'wallet_address'
