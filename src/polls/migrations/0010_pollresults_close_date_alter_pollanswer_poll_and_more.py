# Generated by Django 4.2.2 on 2023-10-08 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0009_pollresults"),
    ]

    operations = [
        migrations.AddField(
            model_name="pollresults",
            name="close_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pollanswer",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poll_related_to_answer",
                to="polls.poll",
            ),
        ),
        migrations.AlterField(
            model_name="pollresults",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="poll_related_to_results",
                to="polls.poll",
            ),
        ),
    ]
