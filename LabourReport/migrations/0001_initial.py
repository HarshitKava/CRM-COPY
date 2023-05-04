# Generated by Django 4.1 on 2022-10-28 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddLabour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LabourCategory', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200, null=True)),
                ('AreaName', models.CharField(choices=[('', 'None'), ('Bhopal', 'Bhopal'), ('SBN', 'SBN'), ('KV', 'KV'), ('DBM', 'DBM'), ('MPZ', 'MPZ'), ('RKP', 'RKP'), ('HBM', 'HBM'), ('ALK', 'ALK'), ('AIIMS', 'AIIMS'), ('Bangalore', 'Bangalore'), ('Casting Yard', 'Casting Yard'), ('Casting Yard QC', 'Casting Yard QC'), ('Casting Yard PM', 'Casting Yard PM')], default='None', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContractorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContractorName', models.CharField(max_length=200, null=True)),
                ('ContractorNumber', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabourOfContractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.addlabour')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Role', models.CharField(choices=[('Site Engineer', 'Site Engineer'), ('Mangement', 'Mangement'), ('Camp Labour Incharge', 'Camp Labour Incharge'), ('Site Labour Incharge', 'Site Labour Incharge'), ('Admin', 'Admin')], max_length=200, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
                ('Password', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StructureName', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SLINight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('NoHelp', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='SLIDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('NoHelp', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='SiteEngNight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
                ('StructureName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.structure')),
            ],
        ),
        migrations.CreateModel(
            name='SiteEngDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='CLINight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('NoHelp', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='CLIDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('NoLabor', models.IntegerField(null=True)),
                ('NoHelp', models.IntegerField(null=True)),
                ('Areaname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.area')),
                ('ContractorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.contractordetail')),
                ('LabourCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LabourReport.labourofcontractor')),
            ],
        ),
    ]