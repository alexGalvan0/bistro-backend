# Generated by Django 4.1.3 on 2022-11-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
