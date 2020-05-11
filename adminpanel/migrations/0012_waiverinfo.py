# Generated by Django 2.1.7 on 2020-05-06 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200425_2003'),
        ('adminpanel', '0011_auto_20200506_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaiverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existingWaiver', models.IntegerField()),
                ('specialWaiver', models.IntegerField()),
                ('totalWaiver', models.IntegerField()),
                ('amountofWaiver', models.IntegerField()),
                ('percentofWaiver', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.SemesterInfo')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentInfo')),
            ],
        ),
    ]
