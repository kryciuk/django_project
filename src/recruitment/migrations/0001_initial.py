# Generated by Django 4.2.2 on 2023-12-17 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobOffer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="description of the position"),
                ),
                ("status", models.BooleanField(help_text="is job offer active?")),
                ("published_date", models.DateField()),
                ("expiry_date", models.DateTimeField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.city",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.company",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations.position",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        help_text="cellular number", max_length=128, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "expected_salary",
                    models.IntegerField(help_text="expected gross salary"),
                ),
                ("cv", models.FileField(upload_to="recruitment/media/cv")),
                (
                    "consent_processing_data",
                    models.BooleanField(
                        help_text="consent to processing of personal data"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "Received"), (1, "Under Review"), (2, "Closed")],
                        default=0,
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job_offer",
                    models.ForeignKey(
                        help_text="reply to job offer",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recruitment.joboffer",
                    ),
                ),
            ],
        ),
    ]
