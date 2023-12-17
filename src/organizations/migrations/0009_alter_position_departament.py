# Generated by Django 4.2.2 on 2023-08-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_alter_position_departament_alter_position_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='departament',
            field=models.TextField(choices=[('Board of Directors', 'Board Of Directors'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Project', 'Project'), ('Design', 'Design'), ('Production', 'Production'), ('Maintenance', 'Maintenance'), ('Store', 'Store'), ('Procurement', 'Procurement'), ('Quality', 'Quality'), ('Inspection', 'Inspection'), ('Packaging', 'Packaging'), ('Finance', 'Finance'), ('Accounting', 'Accounting'), ('Information Technology', 'Information Technology'), ('Research Development', 'Research Development'), ('Human Resource', 'Human Resource'), ('Security', 'Security'), ('Administration', 'Administration')]),
        ),
    ]
