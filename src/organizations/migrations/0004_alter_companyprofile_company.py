# Generated by Django 5.0.1 on 2024-01-27 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0003_alter_department_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyprofile",
            name="company",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="organizations.company"),
        ),
    ]