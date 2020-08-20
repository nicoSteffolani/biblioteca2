from django.contrib import admin
from biblioteca.models import *


class TipoMaterialInline(admin.TabularInline):
    model = TipoMaterial

class RevistaAdmin(admin.ModelAdmin):
    inlines = [TipoMaterialInline,]
    list_display = ['titulo', 'autor','status', 'marca']

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor','status', 'editorial']
    inlines = [TipoMaterialInline, ]


class TipoPersonaInline(admin.TabularInline):
    model = TipoPersona


class AlumnoAdmin(admin.ModelAdmin):
    inlines = [TipoPersonaInline,]
    list_display = ['nombre', 'apellido', 'adeuda', 'matricula']


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'adeuda', 'numEmpleado']
    inlines = [TipoPersonaInline,]


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['fechaReg', 'persona', 'material']


# Register your models here.
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Alumno, AlumnoAdmin, )
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
#admin.site.register(Material, )
#admin.site.register(Persona, )
#admin.site.register(TipoMaterial, )
