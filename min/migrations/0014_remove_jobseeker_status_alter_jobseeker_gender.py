# Generated by Django 4.2.5 on 2023-10-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0013_alter_jobseeker_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='status',
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=None, max_length=6),
        ),
    ]
