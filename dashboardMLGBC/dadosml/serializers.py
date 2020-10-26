from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers
from .models import Dadosml

# Serializers define the API representation.
class DadosMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dadosml
        fields = ['id', 'modelml', 'accuracy', 'prediction','label','features']

