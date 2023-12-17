# Generated by Django 4.2.2 on 2023-10-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0024_rename_departament_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(
                choices=[
                    ("Accounting", "Accounting"),
                    ("Administration", "Administration"),
                    ("Board of Directors", "Board Of Directors"),
                    ("Design", "Design"),
                    ("Finance", "Finance"),
                    ("Human Resource", "Human Resource"),
                    ("Information Technology", "Information Technology"),
                    ("Inspection", "Inspection"),
                    ("Marketing", "Marketing"),
                    ("Maintenance", "Maintenance"),
                    ("Packaging", "Packaging"),
                    ("Procurement", "Procurement"),
                    ("Project", "Project"),
                    ("Production", "Production"),
                    ("Quality", "Quality"),
                    ("Research Development", "Research Development"),
                    ("Sales", "Sales"),
                    ("Security", "Security"),
                    ("Store", "Store"),
                ]
            ),
        ),
        migrations.AlterUniqueTogether(
            name="department",
            unique_together={("name", "company")},
        ),
    ]
