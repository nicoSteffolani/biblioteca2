# Generated by Django 2.2 on 2020-08-19 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20200819_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='alumno',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Alumno'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Libro'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='profesor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Profesor'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='revista',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Revista'),
        ),
    ]
