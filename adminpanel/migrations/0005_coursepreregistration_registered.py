# Generated by Django 2.1.7 on 2020-05-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_courses_totalsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepreregistration',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
