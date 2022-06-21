from django.shortcuts import render
from rest_framework import generics

from .serializers import ApplicationListCreateSerializer
from .models import Application

# Create your views here.
class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListCreateSerializer
