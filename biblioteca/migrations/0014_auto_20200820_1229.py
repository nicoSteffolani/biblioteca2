# Generated by Django 2.2 on 2020-08-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0013_libro_foto_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='foto_portada',
            field=models.ImageField(blank=True, default='/default.jpg', upload_to=''),
        ),
    ]
