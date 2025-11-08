from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from incidents.models import Incident
from incidents.serializers import IncidentSerializer, IncidentStatusUpdateSerializer


class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class IncidentStatusUpdateView(generics.UpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentStatusUpdateSerializer
    http_method_names = ['patch']