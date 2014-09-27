"""
Admin for elcid fields
"""
from django.contrib import admin

from reversion import models as rmodels

admin.site.register(rmodels.Version, admin.ModelAdmin)
admin.site.register(rmodels.Revision, admin.ModelAdmin)
