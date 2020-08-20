from django.contrib import admin
from biblioteca.models import *


class TipoMaterialInline(admin.TabularInline):
    model = TipoMaterial

class RevistaAdmin(admin.ModelAdmin):
    inlines = [TipoMaterialInline,]
    list_display = ['titulo', 'autor','status', 'marca']
    fieldsets = (
        ('Compra',{
            'fields': ('status','marca')
        }),
        ('Datos',{
            'fields': ('titulo', 'autor', 'año')
        }),
    )

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor','status', 'editorial']
    inlines = [TipoMaterialInline, ]

    fieldsets = (
        ('Compra',{
            'fields': ('status','titulo')
        }),
        ('Datos',{
            'fields': ('editorial', 'autor', 'año')
        }),
    )


class TipoPersonaInline(admin.TabularInline):
    model = TipoPersona


class AlumnoAdmin(admin.ModelAdmin):
    inlines = [TipoPersonaInline,]
    list_display = ['nombre', 'apellido', 'adeuda', 'matricula']

    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre','apellido', 'correo', 'telefono')
        }),
        ('Informacion extra',{
            'fields': ('matricula', 'adeuda', 'numLibros')
        }),
    )


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'adeuda', 'numEmpleado']
    inlines = [TipoPersonaInline,]

    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre','apellido', 'correo', 'telefono')
        }),
        ('Informacion extra',{
            'fields': ('numEmpleado', 'adeuda', 'numLibros')
        }),
    )


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
