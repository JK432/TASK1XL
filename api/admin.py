from django.contrib import admin
from . import models



admin.site.register(models.CustomerMaster)
admin.site.register(models.CreateJob)
admin.site.register(models.EmployeeMaster)
admin.site.register(models.JobInfo)

# Register your models here.
