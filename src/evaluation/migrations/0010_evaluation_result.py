# Generated by Django 4.2.2 on 2023-09-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_remove_evaluation_date_evaluation_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='result',
            field=models.JSONField(default=1, verbose_name=''),
            preserve_default=False,
        ),
    ]
