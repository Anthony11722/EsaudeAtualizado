from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from paciente.models import Paciente, Consulta, DocumentoPaciente
from paciente.serializers import PacienteSerializer, ConsultaSerializer, DocumentoPacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        consultas_pendentes = Consulta.get_consultas_pendentes()
        serializer = self.get_serializer(consultas_pendentes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def aprovar(self, request, pk=None):
        consulta = self.get_object()
        consulta.aprovar_consulta()
        serializer = self.get_serializer(consulta)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def negar(self, request, pk=None):
        consulta = self.get_object()
        consulta.negar_consulta()
        serializer = self.get_serializer(consulta)
        return Response(serializer.data)

class DocumentoPacienteViewSet(viewsets.ModelViewSet):
    queryset = DocumentoPaciente.objects.all()
    serializer_class = DocumentoPacienteSerializer