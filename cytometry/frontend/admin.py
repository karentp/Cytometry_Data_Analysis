from django.contrib import admin
from .models import PieDePagina, Textos, Colaborador, SliderImage   # importa tu modelo aquí

admin.site.register(PieDePagina) 
admin.site.register(Textos)  
admin.site.register(Colaborador)
admin.site.register(SliderImage)