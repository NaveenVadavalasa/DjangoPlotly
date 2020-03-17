from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Daily)
# admin.site.register(Weekly)
# admin.site.register(Monthly)



class DailyResource(resources.ModelResource):
    class Meta:
        model = Daily


class DailyAdmin(ImportExportModelAdmin):
    resource_class = DailyResource

admin.site.register(Daily, DailyAdmin)

class WeeklyResource(resources.ModelResource):
    
    class Meta:
        model = Weekly


class WeeklyAdmin(ImportExportModelAdmin):
    resource_class = WeeklyResource

admin.site.register(Weekly, WeeklyAdmin)



class MonthlyResource(resources.ModelResource):
    
    class Meta:
        model = Monthly


class MonthlyAdmin(ImportExportModelAdmin):
    resource_class = MonthlyResource

admin.site.register(Monthly, MonthlyAdmin)
