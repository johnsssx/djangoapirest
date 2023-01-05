from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('crated_at',)