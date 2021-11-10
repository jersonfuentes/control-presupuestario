from django.db import models
from django.contrib.auth.models import User

# App para generar las categorías de cuentas contables
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Create your models here.
class PresupuestoCostoFijo(models.Model):
    item_presupuestario = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)    

    observacion = models.TextField(null=True)
    monto = models.DecimalField(max_digits=50, decimal_places=0,null=True)

    LOAN_STATUS = (
        ('1', 'Por revisar'),
        ('2', 'Aceptado'),
        ('3', 'Con observación'),
    )
    estado = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default='1',verbose_name="Estado del registro")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    def __str__(self):
        return self.observacion

    class Meta:
        verbose_name = "Presupuesto de costo fijo"
        verbose_name_plural = "Presupuestos de costos fijos"

    def listado_periodo(self):
        return ','.join([str(p) for p in self.periodo.all()])
    listado_periodo.short_description = 'Periodo'

    def listado_centro_costo(self):
        return ','.join([str(p) for p in self.periodo.all()])
    listado_centro_costo.short_description = 'CentroCosto'