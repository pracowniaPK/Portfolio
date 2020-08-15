from django.contrib import admin

from .models import Project, ProjectLink, ProjectTag

admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectTag)
