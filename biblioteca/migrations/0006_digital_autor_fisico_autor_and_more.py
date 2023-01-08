# Generated by Django 4.1.4 on 2022-12-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_alter_digital_precio_alter_fisico_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='digital',
            name='autor',
            field=models.CharField(default='desconocido', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fisico',
            name='autor',
            field=models.CharField(default='desconocido', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='digital',
            name='fecha_de_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fisico',
            name='fecha_de_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]