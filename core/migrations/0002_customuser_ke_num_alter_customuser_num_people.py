# Generated by Django 4.1.13 on 2024-02-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ke_num',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='num_people',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
