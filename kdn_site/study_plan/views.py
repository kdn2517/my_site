from django.http import HttpResponse
from django.shortcuts import render

from .models import Subjects


def index(request):
    subjects = Subjects.objects.all()
    return render(request, 'study_plan/index.html', {'subjects': subjects, 'title': 'План '
                                                                                    'изучения'})
