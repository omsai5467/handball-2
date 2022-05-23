from django.contrib import admin

# Register your models here.

from .models import updates,StateAssociations
admin.site.register(updates)
admin.site.register(StateAssociations)
