# Generated by Django 2.1.7 on 2020-05-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_paymentinfo_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepreregistration',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
