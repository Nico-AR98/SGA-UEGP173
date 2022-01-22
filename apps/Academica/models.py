from django.db import models

# Create your models here.

class Carrera(models.Model):

    codigo = models.CharField(max_length=3, primary_key=True)

    nombre = models.CharField(max_length=50)

    duracion= models.PositiveSmallIntegerField(default=5)


class Estudiante (models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F','Femenino'),
        ('M','Masculino'),
        ('O','Otro')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')

    #on_delete=models.CASCADE indica que si se elimina la carrera se eliminan todos los alumnos que pertenecen a esa carrera
    carrera = models.ForeignKey(Carrera,null=False, blank=False,on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    def nombreCompleto(self):
        txt="{0} {1}"
        return txt.format(self.apellido,self.nombre)


class Curso(models.Model):
    #Si no especificamos una primary key para un modelo, Django les asignara una por defecto

    codigo = models.CharField(max_length=6,primary_key=True)

    nombre= models.CharField(max_length=30)

    creditos = models.PositiveSmallIntegerField()

    docente = models.CharField(max_length=80)


class Matricula(models.Model):

    id = models.AutoField(primary_key=True)

    estudiante = models.ForeignKey(Estudiante,null=False,blank=False,on_delete=models.CASCADE) #Se establece clave foránea con la tabla estudiante

    curso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)

    fechaMatricula = models.DateTimeField(auto_now_add=True) #la propiedad auto_now_add añade automáticamente la fecha y hora de la creación del registro"""