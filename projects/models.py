from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')
    show = models.BooleanField(default=True)
    tags = models.ManyToManyField('ProjectTag', blank=True)
    thumbnail = models.CharField(max_length=1000, default='')
    default_link = models.CharField(max_length=1000, default='')
    priority = models.FloatField(default=0)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        hidden = '' if self.show else '(hidden) '
        return hidden + self.title


class ProjectLink(models.Model):
    label = models.CharField(max_length=200)
    target = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '[{}] {} ({})'.format(self.project.title, self.label, self.target)


class ProjectTag(models.Model):
    label = models.CharField(max_length=200)
    color = models.CharField(max_length=10, default='#FFC0CB')

    def __str__(self):
        return self.label
