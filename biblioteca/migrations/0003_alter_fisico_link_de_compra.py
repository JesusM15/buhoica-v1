# Generated by Django 4.1.4 on 2022-12-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_digital_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisico',
            name='link_de_compra',
            field=models.URLField(max_length=2000),
        ),
    ]
