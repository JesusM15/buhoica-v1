# Generated by Django 4.1.4 on 2022-12-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_digital_autor_fisico_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='unidades',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
