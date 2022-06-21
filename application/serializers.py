from rest_framework.serializers import ModelSerializer
from .models import Application

class ApplicationListCreateSerializer(ModelSerializer):
    class Meta:
        model = Application
        exclude = ['id']