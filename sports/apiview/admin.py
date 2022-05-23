from django.contrib import admin

# Register your models here.

# from .models import updates,StateAssociations
from .models import updates,StateAssociations,BoardManageMent,SelectionCommittee,AthletesCommission
admin.site.register(updates)
admin.site.register(BoardManageMent)
admin.site.register(StateAssociations)
admin.site.register(SelectionCommittee)
admin.site.register(AthletesCommission)
