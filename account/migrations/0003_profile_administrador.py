# Generated by Django 4.1.4 on 2022-12-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_direccion_profile_calle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='administrador',
            field=models.BooleanField(default=False),
        ),
    ]
