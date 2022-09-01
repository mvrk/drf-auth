from rest_framework import serializers
from .models import Drf


class DrfSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'color', 'description', 'purchaser', 'created_at')
        model = Drf
