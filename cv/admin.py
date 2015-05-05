from django.contrib import admin
from hvad.admin import TranslatableAdmin
from hvad import forms
from hvad.manager import TranslationManager

from .models import Location, AcademicExperience, WorkExperience, SkillCategory, Skill, Project


class LocationAdmin(TranslatableAdmin):
    objects = TranslationManager()
    objects.prefetch_related('translations')
    form = forms.translatable_modelform_factory('en', Location)
    list_display = ('id', '__str__', 'all_translations',)


admin.site.register(Location, LocationAdmin)


class AcademicExperienceAdmin(TranslatableAdmin):
    objects = TranslationManager()
    objects.prefetch_related('translations')
    form = forms.translatable_modelform_factory('en', AcademicExperience)
    ordering = ('-start_date',)
    list_display = ('__str__', 'start_date', 'end_date', 'all_translations',)

admin.site.register(AcademicExperience, AcademicExperienceAdmin)


class WorkExperienceAdmin(TranslatableAdmin):
    objects = TranslationManager()
    objects.prefetch_related('translations')
    form = forms.translatable_modelform_factory('en', WorkExperience)
    ordering = ('-start_date',)
    list_display = ('__str__', 'start_date', 'end_date', 'all_translations',)

admin.site.register(WorkExperience, WorkExperienceAdmin)


class SkillCategoryAdmin(TranslatableAdmin):
    objects = TranslationManager()
    objects.prefetch_related('translations')
    form = forms.translatable_modelform_factory('en', SkillCategory)
    list_display = ('__str__', 'all_translations',)

admin.site.register(SkillCategory, SkillCategoryAdmin)


class SkillAdmin(admin.ModelAdmin):
    objects = TranslationManager()
    list_display = ('__str__', 'expertise_level', 'category',)

admin.site.register(Skill, SkillAdmin)
admin.site.register(Project)