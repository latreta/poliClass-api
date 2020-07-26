from django.db import models


class Cadeira(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
