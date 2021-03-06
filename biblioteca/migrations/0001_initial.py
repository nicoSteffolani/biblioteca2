# Generated by Django 2.2 on 2020-08-19 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('año', models.IntegerField(null=True)),
                ('status', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(null=True)),
                ('numLibros', models.IntegerField(null=True)),
                ('adeuda', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Persona')),
                ('matricula', models.IntegerField(null=True)),
            ],
            bases=('biblioteca.persona',),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Material')),
                ('editorial', models.CharField(max_length=30)),
            ],
            bases=('biblioteca.material',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Persona')),
                ('numEmpleado', models.IntegerField(null=True)),
            ],
            bases=('biblioteca.persona',),
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Material')),
                ('marca', models.CharField(max_length=30)),
            ],
            bases=('biblioteca.material',),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSal', models.DateField(auto_now=True)),
                ('fechaReg', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Material')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Persona')),
            ],
        ),
    ]
