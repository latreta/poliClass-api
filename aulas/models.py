from django.db import models

# Create your models here.
from cadeiras.models import Cadeira
from discentes.models import Discente
from salas.models import Sala


class Aula(models.Model):
    discente = models.ForeignKey(Discente, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now_add=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s ' % self.disciplina.name, self.disciplina.sala.name, self.disciplina.inicio
