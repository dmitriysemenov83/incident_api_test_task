from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    source_display = serializers.CharField(source='get_source_display', read_only=True)
    
    class Meta:
        model = Incident
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class IncidentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['status']