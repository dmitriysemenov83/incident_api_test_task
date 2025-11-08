from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description_short', 'status', 'source', 'created_at']
    list_filter = ['status', 'source', 'created_at']
    search_fields = ['description']

    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'
