# Generated by Django 4.1.3 on 2022-12-12 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_titulo_vip_titulos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vip',
        ),
    ]
