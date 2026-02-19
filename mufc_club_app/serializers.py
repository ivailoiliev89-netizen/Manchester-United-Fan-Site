from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = Player
        fields = '__all__'
