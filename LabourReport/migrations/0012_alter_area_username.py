# Generated by Django 4.1 on 2022-11-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabourReport', '0011_alter_area_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='Username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]