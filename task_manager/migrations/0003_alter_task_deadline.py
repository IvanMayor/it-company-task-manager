# Generated by Django 4.1.6 on 2023-02-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_task_assignees_alter_worker_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(max_length=12),
        ),
    ]