from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import AdSerializer, AdListSerializer, AdDetailSerializer
from .models import Advertisement

# Create your views here.
class AdListCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Advertisement.objects.select_related('company_id').all()

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdListSerializer
        else:
            return AdSerializer

    def get_filter(self, request, queryset):
        company_name = request.query_params.get('company_name', None)
        position = request.query_params.get('position', None)

        if company_name:
            queryset = queryset.filter(company_id__company_name__contains=company_name)
        if position:
            queryset = queryset.filter(position__contains=position)
        
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_filter(request, self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class AdDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.select_related('company_id').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdDetailSerializer
        else:
            return AdSerializer
    
