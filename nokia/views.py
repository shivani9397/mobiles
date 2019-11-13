from django.shortcuts import render

# Create your views here.
from .models import Nokia
from .serializers import NokiaSerialization
from rest_framework.viewsets import ModelViewSet

#GET GET/{id} POST PUT PATCH DELETE
class NokiaOperations(ModelViewSet):
    queryset = Nokia.objects.all()
    serializer_class = NokiaSerialization