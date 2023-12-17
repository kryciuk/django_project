# Generated by Django 4.2.2 on 2023-09-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0008_alter_answer_picked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='date',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='date_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
