from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def index(request):
    projects = Project.objects.filter(show=True)

    return render(request, 'projects.html', {'projects': projects})
