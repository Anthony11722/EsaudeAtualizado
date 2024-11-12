from rest_framework import routers
from usuario.viewsets import UsuarioViewSet, MedicoViewSet

usuario_router = routers.DefaultRouter()
usuario_router.register('usuario', UsuarioViewSet)
usuario_router.register('medico', MedicoViewSet)
