from rest_framework import serializers
from .models import Paciente, Consulta, DocumentoPaciente

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paciente
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class DocumentoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoPaciente
        fields = ['id', 'paciente', 'titulo', 'arquivo', 'data_upload', 'descricao']