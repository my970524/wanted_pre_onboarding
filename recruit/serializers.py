from dataclasses import fields
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advertisement


class AdSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = ['id']

class AdListSerializer(ModelSerializer):
    company_name = SerializerMethodField()
    country = SerializerMethodField()
    region = SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company_id.company_name
    
    def get_country(self, obj):
        return obj.company_id.country

    def get_region(self, obj):
        return obj.company_id.region

    class Meta:
        model = Advertisement
        exclude = ['content', 'company_id']
    

class AdDetailSerializer(AdListSerializer):
    class Meta(AdListSerializer.Meta):
        exclude = ['company_id']
    
