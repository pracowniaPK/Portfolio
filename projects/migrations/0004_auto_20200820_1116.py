# Generated by Django 3.1 on 2020-08-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200818_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
