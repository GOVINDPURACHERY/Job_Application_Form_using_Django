# Generated by Django 4.2.5 on 2023-10-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('min', '0022_alter_jobseeker_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=None, max_length=6, null=True),
        ),
    ]
