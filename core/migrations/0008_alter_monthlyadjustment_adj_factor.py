# Generated by Django 4.1.13 on 2024-02-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_monthlyadjustment_delete_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyadjustment',
            name='adj_factor',
            field=models.FloatField(default=0.0),
        ),
    ]
