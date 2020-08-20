from django.db import models

# Create your models here.


class Material(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    año = models.IntegerField(null = True)
    status = models.BooleanField(null = True)
    status.boolean = True


    def __str__(self):
        return self.titulo


class Libro(Material):
    editorial = models.CharField(max_length=30)
    #foto_portada = models.ImageField(max_length = 100, upload_to='imagenes/', default='imagenes/default.png', blank=True)


class Revista(Material):
    marca = models.CharField(max_length=30)


class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField(null = True)
    numLibros = models.IntegerField(null = True)
    adeuda = models.BooleanField(null = True)
    adeuda.boolean = True

    def __str__(self):
        return self.nombre + " " + self.apellido

class Alumno(Persona):
    matricula = models.IntegerField(null = True)

class Profesor(Persona):
    numEmpleado = models.IntegerField(null = True)

class TipoMaterial(models.Model):
    libro = models.ForeignKey(Libro, null = True, default = None, on_delete=models.CASCADE)
    revista = models.ForeignKey(Revista, null = True, default = None, on_delete=models.CASCADE)

class TipoPersona(models.Model):
    alumno = models.ForeignKey(Alumno, null = True, default = None, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null = True, default = None, on_delete=models.CASCADE)

    
class Prestamo(models.Model):
    fechaSal = models.DateField(auto_now = True)
    fechaReg = models.DateField()
    material = models.ForeignKey(Material, default = None, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.persona.nombre

