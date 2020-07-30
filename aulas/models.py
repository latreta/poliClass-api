from django.db import models

# Create your models here.
from cadeiras.models import Cadeira
from docentes.models import Docente
from salas.models import Sala


class Aula(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now_add=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.disciplina.name
