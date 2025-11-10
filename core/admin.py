from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'phone')
    search_fields = ('site_name', 'contact_email')
    list_per_page = 10
    ordering = ('site_name',)
