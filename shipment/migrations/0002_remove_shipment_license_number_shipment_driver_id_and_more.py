# Generated by Django 4.1 on 2022-08-13 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_driver'),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='license_number',
        ),
        migrations.AddField(
            model_name='shipment',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.driver'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='truck_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.truck'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
