# Generated by Django 4.1.3 on 2022-11-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_menu_item_spicy_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='spicy_level',
            field=models.CharField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=255),
        ),
    ]
