# Generated by Django 4.1 on 2022-11-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductivityReport', '0008_remove_productivityreport_areaname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productivityreport',
            name='LRid',
            field=models.IntegerField(null=True),
        ),
    ]