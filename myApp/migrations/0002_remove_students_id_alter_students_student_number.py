# Generated by Django 5.0.1 on 2024-06-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AlterField(
            model_name='students',
            name='student_number',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
