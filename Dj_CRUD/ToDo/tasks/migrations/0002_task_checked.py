# Generated by Django 4.2.2 on 2024-01-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
