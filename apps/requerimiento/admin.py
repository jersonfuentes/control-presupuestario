from django.contrib import admin

# Importar y exportar
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Modelos a usar
from django.contrib.auth.models import User
from django.contrib import admin
from apps.requerimiento.models import Requerimiento
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Register your class here.
class RequerimientoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_editable = ['monto',]
    list_filter = ['estado','created','modified',]
    autocomplete_fields = ['item_presupuestario','centro_costo','proveedor','responsable']
    list_per_page = 20

    list_display = [
        'observacion',
        'monto',
        'item_presupuestario',
        'created',
        'modified',
        'estado',
        ]

    fieldsets = (
        #
        ('Identificación del Requerimiento',{
            'fields':(
                ('solicitante',),
                ('proveedor',),
                ('centro_costo',),
                ('codigo_requerimiento',),
                ('responsable',),
                ('item_presupuestario',),
                ('periodo',),                
            ),
        }),

        ('Detalle del Requerimiento',{
            'fields':(
                ('observacion',),
                ('monto',),
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

admin.site.register(Requerimiento, RequerimientoAdmin)