from django.urls import path
from .views import IncidentListCreateView, IncidentStatusUpdateView


app_name = 'incidents'
urlpatterns = [
    path('incidents/', IncidentListCreateView.as_view(), name='incident-list-create'),
    path('incidents/<int:pk>/status/', IncidentStatusUpdateView.as_view(), name='incident-status-update'),
]