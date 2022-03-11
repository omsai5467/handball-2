from django.contrib import admin

# Register your models here.



admin.site.site_header = "Handball India Administration"
from .models import playerdata
admin.site.register(playerdata)
