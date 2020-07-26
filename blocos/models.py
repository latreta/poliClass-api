from django.db import models


class Bloco(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name
