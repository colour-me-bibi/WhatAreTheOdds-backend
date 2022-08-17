from django.contrib import admin

from . import models

admin.site.register(models.Investment)
admin.site.register(models.Tag)
admin.site.register(models.Offer)
admin.site.register(models.Market)
admin.site.register(models.Contract)
admin.site.register(models.UserProfile)
