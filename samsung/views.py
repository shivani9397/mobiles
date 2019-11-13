from django.shortcuts import render

# Create your views here.
from .models import Samsung
from .serializers import SamsungSerialization
from rest_framework.viewsets import ModelViewSet

#GET GET/{id} POST PUT PATCH DELETE
class SamsungOperations(ModelViewSet):
    queryset = Samsung.objects.all()
    serializer_class = SamsungSerialization