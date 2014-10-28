from django.contrib import admin
from app_store.models import *


class ForeignApplicationInline(admin.StackedInline):
	model = ForeignApplication


class ApplicationAdmin(admin.ModelAdmin):
	inlines = [ForeignApplicationInline]

admin.site.register(Application, ApplicationAdmin)
