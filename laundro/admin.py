from django.contrib import admin

from laundro.models import (
    Service,
)


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'desciption', 'create_date',)
    readonly_fields = ('create_date', 'modify_date',)
    search_fields = ['title', 'id']
