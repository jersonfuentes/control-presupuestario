from django.db import models
from django.contrib.auth.models import User

# App para generar las categorías de cuentas contables
from mptt.models import MPTTModel, TreeForeignKey

from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Create your models here.
class Requerimiento(models.Model):
    solicitante = models.CharField(max_length=100)
    proveedor =  models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.CASCADE)
    codigo_requerimiento =  models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    item_presupuestario = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    observacion = models.TextField(null=True)
    monto = models.DecimalField(max_digits=50, decimal_places=0,null=True)
   
    LOAN_STATUS = (
        ('1', 'Por revisar'),
        ('2', 'Aceptado'),
        ('3', 'Con observación'),
    )

    estado = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default='1')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    def __str__(self):
        return self.observacion

    class Meta:
        verbose_name = "Requerimiento ingresado"
        verbose_name_plural = "Requerimientos ingresados"

    def listado_nombre_proveedor(self):
        return ','.join([str(p) for p in self.nombre_proveedor.all()])
    listado_nombre_proveedor.short_description = 'Proveedor'

    def listado_centro_costo(self):
        return ','.join([str(p) for p in self.centro_costo.all()])
    listado_centro_costo.short_description = 'CentroCostos'

    def listado_responsable(self):
        return ','.join([str(p) for p in self.responsable.all()])
    listado_responsable.short_description = 'Responsable'

    def listado_item_presupuestario(self):
        return ','.join([str(p) for p in self.item_presupuestario.all()])
    listado_item_presupuestario.short_description = 'ItemPresupuestario'

    def listado_periodo(self):
        return ','.join([str(p) for p in self.periodo.all()])
    listado_periodo.short_description = 'Periodo'