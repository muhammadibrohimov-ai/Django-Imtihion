from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from .models import Task

# Register your models here.


@admin.register(Task)
class TaskModelAdmin(ImportExportModelAdmin, ModelAdmin):
    list_display_links = ['title', 'deadline']
    list_display = ['title', 'deadline', 'is_complete']
    list_filter = ['is_complete', 'deadline']
    list_editable = ['is_complete']
    ordering = ['created_at']
    search_fields = ['title']

