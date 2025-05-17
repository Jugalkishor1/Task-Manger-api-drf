from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    # readonly_fields=('name',)
    list_display = ("name", "email",)


admin.site.register(User, UserAdmin)
