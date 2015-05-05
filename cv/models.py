from django import forms
from django.db import models

from hvad.models import TranslatableModel, TranslatedFields


class Location(TranslatableModel):
    id = models.CharField(max_length=4, primary_key=True)

    translations = TranslatedFields(
        country = models.CharField(max_length=50),
        city = models.CharField(max_length=50),
    )

    def __str__(self):
        return self.city + " (" + self.country + ")"


class AcademicExperience(TranslatableModel):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, default='')
    grade = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default='')
    location = models.ForeignKey(Location)

    translations = TranslatedFields(
        degree = models.CharField(max_length=65),
        institution = models.CharField(max_length=30),
        further_info = models.TextField(blank=True, default=''),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea},
    }

    def __str__(self):
        return self.degree + " (" + self.institution + ")"


class WorkExperience(TranslatableModel):
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, default='')
    location = models.ForeignKey(Location)

    translations = TranslatedFields(
        role = models.CharField(max_length=50),
        description = models.TextField(blank=True, default=''),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea},
    }

    def __str__(self):
        return self.role + " (" + self.company + ")"


class SkillCategory(TranslatableModel):
    translations = TranslatedFields (
        name = models.CharField(max_length=20),
        description = models.CharField(max_length=50, null=True, blank=True, default=''),
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(SkillCategory)
    expertise_level = models.IntegerField()

    def __str__(self):
        return self.name


class Project(TranslatableModel):
    id = models.CharField(max_length=4, primary_key=True)
    technologies = models.ManyToManyField(Skill)

    translations = TranslatedFields (
        name = models.CharField(max_length=100),
        description = models.CharField(max_length=1000, null=True, blank=True, default=''),
    )

    def __str__(self):
        return self.name