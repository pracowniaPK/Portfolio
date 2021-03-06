# Generated by Django 3.1 on 2020-08-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('label', models.CharField(max_length=200)),
                ('target', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('label', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(default='', max_length=1000)),
                ('show', models.BooleanField(default=True)),
                (
                    'links',
                    models.ManyToManyField(blank=True, to='projects.ProjectLink'),
                ),
                ('tags', models.ManyToManyField(blank=True, to='projects.ProjectTag')),
            ],
        ),
    ]
