from django.contrib import admin
from usuario.models import Usuario
from endereco.models import Endereco

class EnderecoInline(admin.StackedInline):
    model = Endereco
    can_delete = False
    verbose_name_plural = 'Endereço'
    fk_name = 'usuario'  # Define o nome da ForeignKey no Endereco

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'cpf', 'get_endereco')

    # Campos exibidos no formulário de edição de usuários
    fieldsets = (
        ("Informações Pessoais", {'fields': ('first_name', 'last_name', 'email', 'cpf', 'telefone', 'data_nascimento', 'genero')}),
        ("Endereço", {'fields': ('endereco',)}),  # Adiciona o campo endereco
    )

    # Campos exibidos no formulário de criação de novos usuários
    add_fieldsets = (
        ("Informações Pessoais", {'fields': ('first_name', 'last_name', 'email', 'cpf', 'telefone', 'data_nascimento', 'genero')}),
        ("Endereço", {'fields': ('endereco',)}),  # Adiciona o campo endereco
    )

    def get_endereco(self, obj):
        if obj.endereco:
            return f'{obj.endereco.rua}, {obj.endereco.bairro} - {obj.endereco.cep}'
        return 'Sem Endereço'
    get_endereco.short_description = 'Endereço'

# Registra o modelo Endereco no Admin
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'bairro', 'numero_residencia', 'cep')
