from django.db import models

# Create your models here.

class Certificado(models.Model):
    # Datos de la unidad
    dominio = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, help_text='Mercedes Benz, IVECO, etc.')
    modelo = models.CharField(max_length=100)
    anio_patentamiento = models.CharField(max_length=4, verbose_name='Año de patentamiento')
    categoria = models.CharField(
        max_length=6,
        choices=[
            ('N1', 'N1 hasta 3500 kg'),
            ('N2', 'N2 hasta 12000 kg'),
            ('N3', 'N2 hasta 12000 kg')],
        default='N1',
        verbose_name='Categoría')
    vin = models.CharField(max_length=50, verbose_name='Número de chasis (VIN)', default='')
    titular_registral = models.CharField(max_length=100)
    cuit_operador = models.CharField(
        max_length=50,
        verbose_name='CUIT operador',
        help_text='Corresponde al registro RUTA.')

    # Características técnicas
    tipo_vehiculo = models.CharField(
        max_length=6,
        choices=[
            ('CR', 'Camión rígido'),
            ('CT', 'Camión tractor')
        ],
        default='CR',
        verbose_name='Tipo de vehículo')
    altura_vinculacion = models.IntegerField(
        verbose_name='Altura de vinculación',
        help_text='Sólo para camiones tractores. Altura a la que está el vínculo con la unidad arrastrada.',
        default=0)
    marca_vinculacion = models.CharField(max_length=100, verbose_name='Marca de vinculación', default='')
    tipo_carroceria_o_caja_carga = models.TextField(
        verbose_name='Tipo de carrocería o caja de carga',
        help_text='Ej. Camión rígido caja cerrada con plataforma de carga.',
        default='')
    capacidad_total_bodega = models.IntegerField(verbose_name='Capacidad total bodega [m3]', help_text='Volumen de la bodega en número entero.')
    altura_paragolpes = models.IntegerField()
    tipo_tren = models.CharField(
        max_length=6,
        choices=[('2S', '2S'), ('1S-1D', '1S-1D')],
        help_text='Son los ejes indicando si son ruedas simples o dobles. Ej. 1S-1D, es un camión con el primer eje con ruedas simples y el segundo con ruedas dobles.',
        default='2S')
    
    # Dimensiones
    largo = models.IntegerField(help_text='Desde el paragolpes delantero hasta el trasero.')
    ancho = models.IntegerField()
    alto = models.IntegerField(help_text='Desde el piso al techo.')
    voladizo_trasero = models.IntegerField(help_text='Desde el centro del último eje al paragolpes trasero.')
    distancia_primer_eje_al_segundo = models.IntegerField(verbose_name='Distancia 1er eje al 2do', default=0)
    distancia_primer_eje_al_tercero = models.IntegerField(verbose_name='Distancia 1er eje al 3ero', default=0)
    distancia_primer_eje_al_cuarto = models.IntegerField(verbose_name='Distancia 1er eje al 4to', default=0)
    distancia_primer_eje_al_centro = models.IntegerField(
        verbose_name='Distancia 1er eje al centro de carga',
        help_text='Desde el centro del 1er eje a la mitad de la caja de carga o hasta el plato (si es un tractor de carretera).',
        default=0)
    
    # Pesos
    peso_total = models.IntegerField()
    eje_directriz = models.IntegerField(help_text='Peso del eje delantero, del vehículo vacío.')
    total_sin_carga = models.IntegerField(help_text='Peso total del vehículo vacío.')

    # Observaciones
    observaciones = models.TextField()

    # Modificación de LCM (Disp.25/2009)
    tipo_lcm = models.CharField(max_length=100, verbose_name='Tipo', help_text='Ej. Plataforma de carga.')
    marca_lcm = models.CharField(max_length=100, verbose_name='Marca')
    modelo_lcm = models.CharField(max_length=100, verbose_name='Modelo')
    nro_homologacion_lcm = models.CharField(max_length=50, verbose_name='Nro. homologación')
    nro_serie_agregado_lcm = models.CharField(max_length=50, verbose_name='Nro. serie agregado')

    def __str__(self):
        return 'Dominio: %s' % self.dominio
