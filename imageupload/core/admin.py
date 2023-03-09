"""
User interface for admin.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    list_filter = ('is_superuser',)
    ordering = ['id']
    list_display = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),        (
            'Permissions',
            {
                'fields': (
                    'is_superuser',
                )
            }
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'password1',
                    'password2',
                    'is_superuser'
                )
            }
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.AccountTier)
admin.site.register(models.ThumbnailSize)
