from rest_framework import routers
from endereco.viewsets import EnderecoViewSet

endereco_router = routers.DefaultRouter()
endereco_router.register('endereco', EnderecoViewSet)