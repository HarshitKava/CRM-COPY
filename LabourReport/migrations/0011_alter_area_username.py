# Generated by Django 4.1 on 2022-11-21 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LabourReport', '0010_delete_staff_remove_cliday_nohelp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
