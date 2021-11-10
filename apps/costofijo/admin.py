from django.contrib import admin

# Importar y exportar
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Modelos a usar
from apps.costofijo.models import PresupuestoCostoFijo
from django.contrib.auth.models import User
from django.contrib import admin
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Register your class here.
class PresupuestoCostoFijooAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_editable = ['monto','estado',]
    list_filter = ['estado','centro_costo','item_presupuestario','created','modified',]
    autocomplete_fields = ['item_presupuestario','centro_costo',]
    list_per_page = 20

    list_display = [
        'periodo',
        'centro_costo',
        'item_presupuestario',
        'monto',
        'estado',
        'observacion',
        'created',
        'modified',
        ]

    fieldsets = (
        #
        ('Identificación de modificación Costo Fijo',{
            'fields':(
                ('item_presupuestario',),
                ('centro_costo',),
                ('periodo',),
            ),
        }),

        ('Detalle de la modificación',{
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

# Register your models here.
admin.site.register(PresupuestoCostoFijo, PresupuestoCostoFijooAdmin)