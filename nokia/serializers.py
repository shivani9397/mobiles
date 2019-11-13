from rest_framework.serializers import ModelSerializer
from .models import Nokia


class NokiaSerialization(ModelSerializer):

    class Meta:
        model = Nokia
        fields = '__all__'