# Generated by Django 4.1.3 on 2022-11-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_menu_item_spicy_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='spicy_level',
            field=models.PositiveIntegerField(default=0, max_length=1),
        ),
    ]
