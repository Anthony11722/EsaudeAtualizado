from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from endereco.models import Endereco

class Usuario(AbstractUser):
    generos =[
        ('M','Masculino'),
        ('F','Feminino'),
    ]

    telefone = models.CharField(max_length=15)  # formato (xx) xxxxx-xxxx
    cpf = models.CharField(max_length=11, unique=True)  # CPF com 11 dígitos
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices= generos)
    email = models.EmailField(max_length=255, unique=True)  # Já existe no AbstractUser

    #chamando endereço
    endereco = models.ForeignKey(Endereco, verbose_name=("endereço"), on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  # Define um related_name único
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',  # Define um related_name único
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Medico(Usuario):
    especialidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return f'Dr(a). {self.first_name} {self.last_name} - {self.especialidade}'