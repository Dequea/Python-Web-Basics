# Generated by Django 3.2.4 on 2021-06-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]