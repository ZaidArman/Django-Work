from django.contrib import admin
from jobs.models import jobHiring
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ("jobTitle", "address", "salary")


admin.site.register(jobHiring, JobAdmin)


# or

# class JobAdmin(admin.ModelAdmin):
#         model = jobHiring
#         fields_display = ("name", "address", "salary")

# @admin.register(jobHiring)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ("name", "address", "salary")