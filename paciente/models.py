from django.db import models
from usuario.models import Usuario

'''

CRIAR API
passo 1 Criar Models
passo 2 Criar o Serializers
passo 3 Criar viewsets
passo 4 criar routers
passo 5 incluir a rota na ulrs.py do setup
passo 6 colocar o admin

'''

class Paciente(Usuario):

    plano_saude = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = [
            'first_name' 
        ]

    def __str__(self):
        return f'Paciente: {self.first_name} {self.last_name}'

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADO', 'Aprovado'),
        ('NEGADO', 'Negado')
    ]
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas")
    medico = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="consultas_medico")
    data_horario = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering = ['data_horario']

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data_horario}"

    @classmethod
    def get_consultas_pendentes(cls):
        return cls.objects.filter(status='PENDENTE')

    def aprovar_consulta(self):
        self.status = 'APROVADO'
        self.save()

    def negar_consulta(self):
        self.status = 'NEGADO'
        self.save()

class DocumentoPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="documentos")
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentos_pacientes/')
    data_upload = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Documento do Paciente'
        verbose_name_plural = 'Documentos dos Pacientes'
        ordering = ['-data_upload']

    def __str__(self):
        return f"Documento {self.titulo} - {self.paciente}"
