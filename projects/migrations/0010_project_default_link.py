# Generated by Django 3.1.1 on 2020-09-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200902_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='default_link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
