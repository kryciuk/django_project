# Generated by Django 4.2.2 on 2023-08-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_interested_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interested_in',
            field=models.IntegerField(choices=[(0, 'BOARD_OF_DIRECTORS'), (1, 'MARKETING'), (2, 'Sales'), (3, 'Project'), (4, 'Design'), (5, 'Production'), (6, 'Maintenance'), (7, 'Store'), (8, 'Procurement'), (9, 'Quality'), (10, 'Inspection'), (11, 'Packaging'), (12, 'Finance'), (13, 'ACCOUNTING'), (14, 'Information Technology'), (15, 'Research Development'), (16, 'Human Resource'), (17, 'Security'), (18, 'Administration')]),
        ),
    ]
