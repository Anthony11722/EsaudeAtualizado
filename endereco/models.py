from django.db import models


class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero_residencia = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)  # formato xxxxx-xxx (com hífen)
    

    def __str__(self):
        return f'{self.rua}, {self.bairro} - {self.cep}'