from rest_framework.serializers import ModelSerializer
from .models import Company, Advertisement

class AdSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        exclude = ['id']