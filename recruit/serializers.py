from dataclasses import fields
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advertisement, Company


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
    other_ads = SerializerMethodField()

    def get_other_ads(sefl, obj):
        company_id = obj.company_id.id
        company = Company.objects.get(id=company_id)
        ads = company.ads.all().exclude(id=obj.id)
        datas = []
        for ad in ads:
            data = ad.id
            datas.append(data)
        return datas        
        

    class Meta(AdListSerializer.Meta):
        exclude = ['company_id']


