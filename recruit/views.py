from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import AdsCreateSerializer

# Create your views here.
class AdsCreateView(generics.CreateAPIView):
    serializer_class = AdsCreateSerializer
