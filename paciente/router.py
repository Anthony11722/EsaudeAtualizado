from rest_framework import routers
from paciente.viewsets import PacienteViewSet, ConsultaViewSet, DocumentoPacienteViewSet

paciente_router = routers.DefaultRouter()
paciente_router.register('paciente', PacienteViewSet)
paciente_router.register('consulta', ConsultaViewSet)
paciente_router.register('documentos', DocumentoPacienteViewSet)