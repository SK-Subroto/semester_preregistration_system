# Generated by Django 2.1.7 on 2020-05-06 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0010_courseregistration_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waiverinfo',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='waiverinfo',
            name='student',
        ),
        migrations.DeleteModel(
            name='WaiverInfo',
        ),
    ]
