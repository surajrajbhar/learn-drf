# Generated by Django 3.0.1 on 2019-12-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufactures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField()),
                ('shipping_cost', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Manufactures')),
            ],
        ),
    ]
