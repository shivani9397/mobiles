from rest_framework.serializers import ModelSerializer
from .models import Samsung


class SamsungSerialization(ModelSerializer):

    class Meta:
        model = Samsung
        fields = '__all__'