# Generated by Django 5.0.3 on 2024-04-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0008_delete_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]