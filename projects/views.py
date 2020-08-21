from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def index(request):
    if 'tag' in request.GET:
        projects = Project.objects.filter(
            show=True, 
            tags__label__iexact=request.GET['tag'],
        )
        if request.GET.get('strict') == 'false':
            projects_tail = (Project.objects
                .filter(show=True)
                .exclude(tags__label__iexact=request.GET['tag'])
            )
            # projects = list(chain(projects, projects_tail))
            projects = projects | projects_tail
    else:
        projects = Project.objects.filter(show=True)

    return render(request, 'projects.html', {'projects': projects, 'x_tag': request.GET.get('tag')})
