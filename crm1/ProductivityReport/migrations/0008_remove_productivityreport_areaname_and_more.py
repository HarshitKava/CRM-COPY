# Generated by Django 4.1 on 2022-11-28 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductivityReport', '0007_remove_productivityreport_categoryname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productivityreport',
            name='Areaname',
        ),
        migrations.RemoveField(
            model_name='productivityreport',
            name='StructureName',
        ),
    ]
