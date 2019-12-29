# Generated by Django 3.0.1 on 2019-12-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='joboffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=500)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
