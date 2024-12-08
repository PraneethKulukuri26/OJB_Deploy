# Generated by Django 5.0.2 on 2024-03-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employermodule', '0002_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='jobs', to='employermodule.applicant'),
        ),
    ]