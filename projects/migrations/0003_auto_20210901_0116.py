# Generated by Django 3.2.6 on 2021-09-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210831_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='descrition',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]