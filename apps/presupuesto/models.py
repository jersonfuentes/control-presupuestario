from django.db import models
from django.contrib.auth.models import User

# App para generar las categorías de cuentas contables
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.      
class CentroCosto(MPTTModel):
    codigo_centro_costo = models.CharField(max_length=15, unique=True)
    nombre_centro_costo = models.TextField()

    parent = TreeForeignKey('self',null=True,blank=True,related_name='children',db_index=True,on_delete=models.CASCADE,verbose_name='Depende de')
    active = models.BooleanField(default=True,null=False,blank=False,verbose_name='Estado')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class MPTTMeta: 
        order_insertion_by = ['nombre_centro_costo']
    
    def __str__(self):
        return str(self.codigo_centro_costo) + ' - ' +self.nombre_centro_costo

    class Meta:
        verbose_name = 'Centro de Costo'
        verbose_name_plural = 'Centros de Costos'

class Cuenta(MPTTModel):
    codigo_cuenta = models.CharField(max_length=15, unique=True)
    nombre_cuenta = models.TextField()
    
    parent = TreeForeignKey('self',null=True,blank=True,related_name='children',db_index=True,on_delete=models.CASCADE,verbose_name='Depende de')
    active = models.BooleanField(default=True,null=False,blank=False,verbose_name='Estado')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class MPTTMeta: 
        order_insertion_by = ['nombre_cuenta']

    def __str__(self):
        return str(self.codigo_cuenta) + ' - ' +self.nombre_cuenta

    class Meta:
        verbose_name = 'Cuenta Contable'
        verbose_name_plural = 'Cuentas Contables'

class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    #is_admin = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cargo
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

class Periodo(models.Model):
    periodo = models.CharField(max_length=50)

    active = models.BooleanField(default=True,null=False,blank=False,verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.periodo

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

class Proyecto(MPTTModel):
    codigo_proyecto = models.CharField(max_length=15, unique=True)
    nombre_proyecto = models.TextField()

    parent = TreeForeignKey('self',null=True,blank=True,related_name='children',db_index=True,on_delete=models.CASCADE,verbose_name='Depende de')
    active = models.BooleanField(default=True,null=False,blank=False,verbose_name='Estado')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class MPTTMeta: 
        order_insertion_by = ['nombre_proyecto']

    def __str__(self):
        return self.nombre_proyecto

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

class Proveedor(models.Model):
    codigo_proveedor = models.CharField(max_length=15, unique=True,verbose_name='RUT del Proveedor')
    nombre_proveedor = models.CharField(max_length=300, unique=True)
    email = models.EmailField()
    movil = models.CharField(max_length=15, unique=True)
    direccion_proveedor = models.TextField(max_length=100, unique=True)

    LOAN_STATUS = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )

    estado = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default='1',verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.codigo_proveedor) + ' - ' +self.nombre_proveedor
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Responsable(models.Model):
    codigo_responsable = models.CharField(max_length=15, unique=True, verbose_name='RUT del responsable')
    nombre_responsable = models.CharField(max_length=300, unique=True)
    email = models.EmailField()
    movil = models.CharField(max_length=15, unique=True)

    LOAN_STATUS = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )

    estado = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default='1')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.codigo_responsable) + ' - ' +self.nombre_responsable

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'