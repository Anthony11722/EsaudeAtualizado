import pytest
from django.contrib.admin.sites import AdminSite
from usuario.models import Usuario
from endereco.models import Endereco
from usuario.admin import UsuarioAdmin
from usuario.admin import EnderecoAdmin

admin_site = AdminSite()

@pytest.fixture
def usuario():
    return Usuario(
        first_name="João",
        last_name="Silva",
        email="joao.silva@example.com",
        cpf="12345678901",
        telefone="(11) 98765-4321",
        data_nascimento="1990-01-01",
        genero="M"
    )

@pytest.fixture
def endereco():
    return Endereco(
        rua="Rua das Flores",
        bairro="Centro",
        numero_residencia="100",
        cep="12345-678",
        usuario=Usuario
    )

@pytest.fixture
def usuario_admin():
    return UsuarioAdmin(Usuario, admin_site)

@pytest.fixture
def endereco_admin():
    return EnderecoAdmin(Endereco, admin_site)

def test_usuario_admin_list_display(usuario_admin):

    assert usuario_admin.list_display == ('first_name', 'last_name', 'email', 'cpf', 'get_endereco')

def test_endereco_admin_list_display(endereco_admin):

    assert endereco_admin.list_display == ('rua', 'bairro', 'numero_residencia', 'cep')

def test_usuario_admin_fieldsets(usuario_admin):

    expected_fieldsets = (
        ("Informações Pessoais", {'fields': ('first_name', 'last_name', 'email', 'cpf', 'telefone', 'data_nascimento', 'genero')}),
        ("Endereço", {'fields': ('endereco',)}),
    )
    assert usuario_admin.fieldsets == expected_fieldsets
    assert usuario_admin.add_fieldsets == expected_fieldsets

def test_usuario_admin_get_endereco(usuario, endereco, usuario_admin):
  
    usuario.endereco = endereco
    assert usuario_admin.get_endereco(usuario) == 'Rua das Flores, Centro - 12345-678'

    usuario.endereco = None
    assert usuario_admin.get_endereco(usuario) == 'Sem Endereço'
