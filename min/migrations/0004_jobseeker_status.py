# Generated by Django 4.2.5 on 2023-10-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0003_alter_jobseeker_country_alter_jobseeker_job_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='status',
            field=models.CharField(default='test', max_length=10),
        ),
    ]
