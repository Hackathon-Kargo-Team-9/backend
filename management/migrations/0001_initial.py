# Generated by Django 4.1 on 2022-08-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('driver_license', models.CharField(max_length=15)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
