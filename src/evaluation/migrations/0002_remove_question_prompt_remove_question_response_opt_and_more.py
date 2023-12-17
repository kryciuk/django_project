# Generated by Django 4.2.2 on 2023-07-30 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='prompt',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response_opt',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='questionare',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='evaluation.questionnaire'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='evaluation.question')),
            ],
        ),
    ]
