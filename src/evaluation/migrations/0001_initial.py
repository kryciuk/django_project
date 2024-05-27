# Generated by Django 5.0.6 on 2024-05-27 18:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organizations", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("answer", models.CharField(max_length=200)),
                ("score", models.IntegerField(blank=True, null=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="answers", to="evaluation.question"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Questionnaire",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("status", models.BooleanField(default=True, help_text="will this questionnaire be ever used again")),
                ("type", models.TextField(choices=[("Evaluation", "Evaluation"), ("Poll", "Poll")])),
                (
                    "company",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="organizations.company"),
                ),
                (
                    "created_by",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="questionnaire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="questions", to="evaluation.questionnaire"
            ),
        ),
        migrations.CreateModel(
            name="Evaluation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_created", models.DateField()),
                ("date_end", models.DateTimeField()),
                ("result_employee", models.JSONField(blank=True, null=True, verbose_name="")),
                ("result_manager", models.JSONField(blank=True, null=True, verbose_name="")),
                (
                    "status_employee",
                    models.BooleanField(default=False, help_text="true if evaluation filled by the employee"),
                ),
                (
                    "status_manager",
                    models.BooleanField(default=False, help_text="true if evaluation filled by the manager"),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manager",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "questionnaire",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="evaluation.questionnaire"),
                ),
            ],
        ),
    ]
