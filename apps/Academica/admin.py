from django.contrib import admin
from apps.Academica.models import * #Importo los modelos

# Aqui registro los modelos creados para poder administrarlos desde el panel de administración.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)