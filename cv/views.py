from django.shortcuts import render
from hvad.manager import TranslationManager

from .models import WorkExperience


def index(request):
    work_experiences = WorkExperience.objects.order_by('-start_date')
    return render(request, 'cv/index.html', {'work_experiences': work_experiences})
