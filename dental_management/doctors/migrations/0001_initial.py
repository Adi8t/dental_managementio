# Generated by Django 5.1.1 on 2024-09-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npi', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('affiliated_clinics', models.ManyToManyField(to='clinics.clinic')),
                ('offered_procedures', models.ManyToManyField(to='doctors.procedure')),
            ],
        ),
    ]
