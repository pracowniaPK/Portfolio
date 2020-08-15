from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')
    show = models.BooleanField(default=True)
    tags = models.ManyToManyField('ProjectTag', blank=True)
    links = models.ManyToManyField('ProjectLink', blank=True)
    thumbnail = models.ImageField(upload_to='images/', default='media\images\default.png')

    def __str__(self):
        hidden = '' if self.show else '(hidden) '
        return hidden + self.title

class ProjectLink(models.Model):
    label = models.CharField(max_length=200)
    target = models.CharField(max_length=1000)

    def __str__(self):
        return '{} ({})'.format(self.label, self.target)

class ProjectTag(models.Model):
    label = models.CharField(max_length=200)
    color = models.CharField(max_length=10)
    
    def __str__(self):
        return self.label
