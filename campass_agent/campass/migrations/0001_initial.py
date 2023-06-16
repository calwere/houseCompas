# Generated by Django 4.2.2 on 2023-06-12 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('house_type', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('beds', models.CharField(max_length=100)),
                ('baths', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='houses')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campass.agent')),
            ],
        ),
    ]