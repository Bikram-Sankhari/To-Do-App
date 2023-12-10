from django.contrib import admin
from .models import Tasks


class TaskAdmin(admin.ModelAdmin):
    list_display = ["description", 'is_completed', 'created_at', 'updated_at']


admin.site.register(Tasks, TaskAdmin)
