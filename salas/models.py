from django.db import models

from blocos.models import Bloco


class Sala(models.Model):
    name = models.CharField(max_length=3)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)

    def __str__(self):
        return self.bloco.name + self.name
