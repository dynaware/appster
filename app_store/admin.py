from django.contrib import admin
from app_store.models import *


class ForeignApplicationInline(admin.TabularInline):
	model = ForeignApplication
	extra = 1


class ReviewInline(admin.TabularInline):
	model = Review
	extra = 1


class ApplicationAdmin(admin.ModelAdmin):
	inlines = [ForeignApplicationInline, ReviewInline]


class ApplicationListEntryInline(admin.TabularInline):
	model = ApplicationListEntry
	extra = 1


class ApplicationListAdmin(admin.ModelAdmin):
	inlines = [ApplicationListEntryInline]

admin.site.register(ApplicationList, ApplicationListAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ForeignRepo)
admin.site.register(Category)
