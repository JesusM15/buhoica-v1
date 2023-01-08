# Generated by Django 4.1.4 on 2022-12-30 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblioteca', '0009_digital_show_fisico_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario_f',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fcomments', to='biblioteca.fisico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userf_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_d',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuerpo', models.TextField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dcomments', to='biblioteca.digital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userd_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
