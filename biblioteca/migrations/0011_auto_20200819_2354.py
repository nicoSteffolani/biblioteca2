# Generated by Django 2.2 on 2020-08-20 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0010_auto_20200819_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='foto_portada',
            field=models.ImageField(blank=True, default='imagenes/default.png', upload_to='imagenes/'),
        ),
    ]