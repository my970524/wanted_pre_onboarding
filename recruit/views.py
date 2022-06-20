from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import AdSerializer, AdListSerializer
from .models import Advertisement

# Create your views here.
class AdListCreateView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdListSerializer
        else:
            return AdSerializer

class AdUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer

