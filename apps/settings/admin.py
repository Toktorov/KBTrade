from django.contrib import admin

from apps.settings.models import Setting, Contact, News, Benefit, Team, Review

# Register your models here.
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'job_title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')