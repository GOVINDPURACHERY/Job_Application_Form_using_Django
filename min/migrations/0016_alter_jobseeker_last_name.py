# Generated by Django 4.2.5 on 2023-10-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0015_alter_jobseeker_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
