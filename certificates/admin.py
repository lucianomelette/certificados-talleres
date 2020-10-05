from django.contrib import admin

from .models import Certificado

# Register your models here.

class CertificadoAdmin(admin.ModelAdmin):
    # Datos de la unidad
    fieldsets = (
        ('Datos de la unidad', {
            'fields': ('dominio', 'marca', 'modelo', 'anio_patentamiento', 'categoria', 'vin', 'titular_registral', 'cuit_operador')
        }),
        ('Caraterísticas técnicas', {
            'fields': ('tipo_vehiculo', 'altura_vinculacion', 'marca_vinculacion', 'tipo_carroceria_o_caja_carga', 'capacidad_total_bodega', 'altura_paragolpes', 'tipo_tren')
        }),
        ('Dimensiones', {
            'fields': ('largo', 'ancho', 'alto', 'voladizo_trasero', 'distancia_primer_eje_al_segundo', 'distancia_primer_eje_al_tercero', 'distancia_primer_eje_al_cuarto', 'distancia_primer_eje_al_centro')
        }),
        ('Pesos', {
            'fields': ('peso_total', 'eje_directriz', 'total_sin_carga', 'observaciones')
        }),
        ('Modificación de LCM (Disp.25/2009)', {
            'fields': ('tipo_lcm', 'marca_lcm', 'modelo_lcm', 'nro_homologacion_lcm', 'nro_serie_agregado_lcm')
        })
    )

admin.site.register(Certificado, CertificadoAdmin)