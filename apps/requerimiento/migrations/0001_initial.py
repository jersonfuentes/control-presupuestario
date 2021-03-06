# Generated by Django 3.1.4 on 2021-08-16 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('presupuesto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitante', models.CharField(max_length=100)),
                ('codigo_requerimiento', models.CharField(max_length=100)),
                ('observacion', models.TextField(null=True)),
                ('monto', models.DecimalField(decimal_places=0, max_digits=50, null=True)),
                ('estado', models.CharField(blank=True, choices=[('1', 'Por revisar'), ('2', 'Aceptado'), ('3', 'Con observación')], default='1', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('centro_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.centrocosto')),
                ('item_presupuestario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.cuenta')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.periodo')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.proveedor')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuesto.responsable')),
            ],
            options={
                'verbose_name': 'Requerimiento ingresado',
                'verbose_name_plural': 'Requerimientos ingresados',
            },
        ),
    ]
