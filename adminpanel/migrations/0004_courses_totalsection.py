# Generated by Django 2.1.7 on 2020-04-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='totalSection',
            field=models.IntegerField(null=True),
        ),
    ]
