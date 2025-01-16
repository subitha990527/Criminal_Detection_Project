from django.contrib import admin

# Register your models here.
from detectionapp import models

admin.site.register(models.Login)
admin.site.register(models.Policereg)
admin.site.register(models.Criminalreg)
admin.site.register(models.Publicreg)
admin.site.register(models.Complaint)