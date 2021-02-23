from django.contrib import admin
from . import models


class FileInLine(admin.TabularInline):
    model = models.File
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_stamp')
    inlines = [FileInLine]


class FileAdmin(admin.ModelAdmin):
    list_display = ('company', 'file_model_name', 'time_stamp')


class HistoricAdmin(admin.ModelAdmin):
    list_display = ('company', 'file', 'file_name', 'status')


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.File, FileAdmin)
admin.site.register(models.Historic, HistoricAdmin)

