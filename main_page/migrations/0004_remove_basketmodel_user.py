# Generated by Django 4.0.6 on 2023-09-16 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_remove_basketmodel_meal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketmodel',
            name='user',
        ),
    ]
