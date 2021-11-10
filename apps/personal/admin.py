from django.contrib import admin

# Importar y exportar
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Modelos a usar
from apps.personal.models import PresupuestoPersona
from django.contrib.auth.models import User
from django.contrib import admin
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Register your class here.
class PresupuestoPersonaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter = ['estado','created','modified',]
    list_per_page = 20

    list_display = [
        'nombre_analisis',
        'observacion',
        'periodo',
        ]

    fieldsets = (
        #
        ('Identificación de registro de presupuesto de personas',{
            'fields':(
                ('nombre_analisis',),
                ('observacion',),
                ('periodo',),
            ),
        }),

        ('Archivos de análisis',{
            'fields':(
                #('archivo',),
            ),
        }),

        ('Identificación del registro',{
            'classes':('collapse',),
            'fields':(
                ('created','modified','estado',),
                ),
        }),
    )
    readonly_fields = ('created','modified',)

# Register your models here.
admin.site.register(PresupuestoPersona, PresupuestoPersonaAdmin)