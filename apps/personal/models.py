from django.db import models
from django.contrib.auth.models import User

# App para generar las categorías de cuentas contables
from apps.presupuesto.models import Cuenta, CentroCosto, Funcionario, Periodo, Proyecto, Proveedor, Responsable

# Create your models here.
class PresupuestoPersona(models.Model):
    nombre_analisis = models.CharField(max_length=300, unique=True)
    observacion = models.TextField(null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)    

    #archivo = models.FileField(upload_to='/home/soporte/sistema/archivos/% Y/% m/% d/')

    LOAN_STATUS = (
        ('1', 'Por revisar'),
        ('2', 'Aceptado'),
        ('3', 'Con observación'),
    )

    estado = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default='1',verbose_name="Estado del registro")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    modified = models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre_analisis

    class Meta:
        verbose_name = "Presupuesto de personas"
        verbose_name_plural = "Presupuestos de personas"

    def listado_periodo(self):
        return ','.join([str(p) for p in self.periodo.all()])
    listado_periodo.short_description = 'Periodo'