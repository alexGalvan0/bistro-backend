# Generated by Django 4.1.3 on 2022-11-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
