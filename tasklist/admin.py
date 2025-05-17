from django.contrib import admin
from .models import Tasklist


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status",)


admin.site.register(Tasklist, TaskAdmin)
