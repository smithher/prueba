# Generated by Django 4.1.3 on 2022-12-11 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(blank=True, max_length=100)),
                ('requisitos1', models.CharField(blank=True, max_length=100)),
                ('requisitos2', models.CharField(blank=True, max_length=100)),
                ('requisitos3', models.CharField(blank=True, max_length=100)),
                ('numero', models.CharField(blank=True, max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=99999)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categorias', models.ManyToManyField(to='blog.categoria')),
            ],
            options={
                'verbose_name': 'vip',
                'verbose_name_plural': 'vips',
            },
        ),
    ]
