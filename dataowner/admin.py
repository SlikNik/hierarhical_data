from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dataowner.models import DataOwner

class OwnerUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'About Owner',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'display_name',
                ),
            },
        ),
    )

admin.site.register(DataOwner, OwnerUserAdmin)