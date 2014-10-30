from django.contrib import admin
from app_store.models import *


class ForeignApplicationInline(admin.TabularInline):
	model = ForeignApplication
	extra = 1


class ApplicationAdmin(admin.ModelAdmin):
	inlines = [ForeignApplicationInline]

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ForeignRepo)
admin.site.register(Category)
