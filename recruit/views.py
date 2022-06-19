from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import AdSerializer
from .models import Advertisement

# Create your views here.
class AdCreateView(generics.CreateAPIView):
    serializer_class = AdSerializer

class AdUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer
