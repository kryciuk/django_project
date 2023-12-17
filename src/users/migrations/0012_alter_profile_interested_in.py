# Generated by Django 4.2.2 on 2023-08-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_interested_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interested_in',
            field=models.TextField(choices=[('Board of Directors', 'Board Of Directors'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Project', 'Project'), ('Design', 'Design'), ('Production', 'Production'), ('Maintenance', 'Maintenance'), ('Store', 'Store'), ('Procurement', 'Procurement'), ('Quality', 'Quality'), ('Inspection', 'Inspection'), ('Packaging', 'Packaging'), ('Finance', 'Finance'), ('Accounting', 'Accounting'), ('Information Technology', 'Information Technology'), ('Research Development', 'Research Development'), ('Human Resource', 'Human Resource'), ('Security', 'Security'), ('Administration', 'Administration')]),
        ),
    ]
