# Generated by Django 4.0.6 on 2023-09-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='menu/images')),
                ('meal_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('pice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
