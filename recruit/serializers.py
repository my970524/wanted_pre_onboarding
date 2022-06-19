from rest_framework.serializers import ModelSerializer
from .models import Company, Advertisement

class AdsCreateSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = ['id']