from django.db import models

class MiModelo(models.Model):
    campo_texto = models.CharField(max_length=200)
    campo_numero = models.IntegerField(default=0)

    def __str__(self):
        return self.campo_texto