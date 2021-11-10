from django.contrib import admin

# App para generar las categorías de cuentas contables
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeRelatedFieldListFilter

# Importar y exportar
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

# Modelos a usar
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Register your class here.

#Centros de costos
class CentroCostoResource(resources.ModelResource):
    parent = fields.Field( 
        column_name='parent',
        attribute='parent',
        widget = widgets.ForeignKeyWidget(CentroCosto, 'codigo_centro_costo'))

    class Meta:
        model = CentroCosto
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('codigo_centro_costo','nombre_centro_costo','parent')
        fields = ('codigo_centro_costo','nombre_centro_costo','parent')

@admin.register(CentroCosto)
class CentroCostoAdmin(ImportExportMixin,DraggableMPTTAdmin):
    resource_class = CentroCostoResource
    list_display = ['tree_actions','codigo_centro_costo','indented_title','active']
    list_editable = ['active']
    list_filter = ['active']
    search_fields = ['codigo_centro_costo','nombre_centro_costo']
    autocomplete_fields = ['parent']

    fieldsets = (
        #
        ('Registro de Centros de Costos',{
            'fields':(
                ('codigo_centro_costo',),
                ('nombre_centro_costo',),
                ('parent',),
            ),
        }),

        ('Identificación del registro',{
            'classes':('collapse',),
            'fields':(
                ('created','modified','active',),
                ),
        }),
    )
    readonly_fields = ('created','modified',)

#Cuentas
class CuentaResource(resources.ModelResource):
    parent = fields.Field( 
        column_name='parent',
        attribute='parent',
        widget = widgets.ForeignKeyWidget(Cuenta, 'codigo_cuenta'))

    class Meta:
        model = Cuenta
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('codigo_cuenta','nombre_cuenta','parent')
        fields = ('codigo_cuenta','nombre_cuenta','parent')

@admin.register(Cuenta)
class CuentaAdmin(ImportExportMixin,DraggableMPTTAdmin):
    resource_class = CuentaResource
    list_display = ['tree_actions','codigo_cuenta','indented_title','active']
    list_editable = ['active']
    list_filter = ['active']
    search_fields = ['codigo_cuenta','nombre_cuenta']
    autocomplete_fields = ['parent']

    fieldsets = (
        #
        ('Registro de Cuenta Contable',{
            'fields':(
                ('codigo_cuenta',),
                ('nombre_cuenta',),
                ('parent',),
            ),
        }),

        ('Identificación del registro',{
            'classes':('collapse',),
            'fields':(
                ('created','modified','active',),
                ),
        }),
    )
    readonly_fields = ('created','modified',)

#Funcionario
class FuncionarioResource(resources.ModelResource):
    class Meta:
        model = Funcionario

class FuncionarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['usuario', 'cargo']
    resources_class = FuncionarioResource

class FuncionarioInline(admin.StackedInline):
    model = Funcionario
    can_delete = False
    verbose_name = Funcionario

class UserAdmin(ImportExportModelAdmin,BaseUserAdmin):
    inlines = (FuncionarioInline,)
    list_editable = ['is_staff']

class UserResource(resources.ModelResource):
    class Meta:
        model = User

#Periodo
class PeriodoResource(resources.ModelResource):
    class Meta:
        model = Periodo

class PeriodoAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['periodo']
    search_fields = ['periodo']
    resources_class = PeriodoResource

    fieldsets = (
        #
        ('Registro de Periodos',{
            'fields':(
                ('periodo',),
            ),
        }),

        ('Identificación del registro',{
            'classes':('collapse',),
            'fields':(
                ('created','modified','active',),
                ),
        }),
    )
    readonly_fields = ('created','modified',)

#Proyecto
class ProyectoResource(resources.ModelResource):
    parent = fields.Field( 
        column_name='parent',
        attribute='parent',
        widget = widgets.ForeignKeyWidget(Proyecto, 'codigo_proyecto'))

    class Meta:
        model = Proyecto
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('codigo_proyecto','nombre_proyecto','parent')
        fields = ('codigo_proyecto','nombre_proyecto','parent')

@admin.register(Proyecto)
class ProyectoAdmin(ImportExportMixin,DraggableMPTTAdmin):
    resource_class = ProyectoResource
    list_display = ['tree_actions','codigo_proyecto','indented_title','active']
    list_editable = ['active']
    list_filter = ['active']
    search_fields = ['codigo_proyecto','nombre_proyecto']
    autocomplete_fields = ['parent']

    fieldsets = (
        #
        ('Registro de Proyecto',{
            'fields':(
                ('codigo_proyecto',),
                ('nombre_proyecto',),
                ('parent',),
            ),
        }),

        ('Identificación del registro',{
            'classes':('collapse',),
            'fields':(
                ('created','modified','active',),
                ),
        }),
    )
    readonly_fields = ('created','modified',)

#Proveedor
class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['codigo_proveedor', 'nombre_proveedor']
    search_fields = ['codigo_proveedor','nombre_proveedor']
    resources_class = ProveedorResource

    fieldsets = (
        #
        ('Registro de proveedor',{
            'fields':(
                ('codigo_proveedor',),
                ('nombre_proveedor',),
                ('email','movil',),
                ('direccion_proveedor',),
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

#Responsable
class ResponsableResource(resources.ModelResource):
    class Meta:
        model = Responsable

@admin.register(Responsable)
class ResponsableAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['codigo_responsable', 'nombre_responsable']
    search_fields = ['codigo_responsable','nombre_responsable']
    resources_class = ResponsableResource

    fieldsets = (
        #
        ('Registro de proveedor',{
            'fields':(
                ('codigo_responsable',),
                ('nombre_responsable',),
                ('email','movil',),
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
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Periodo, PeriodoAdmin)