from django.contrib import admin
from paciente.models import Paciente, DocumentoPaciente, Consulta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cpf', 'email')
    # fieldsets = (("informações pessoais"), {"fields": ("first_name", "last_name")}),


@admin.register(DocumentoPaciente)
class DocumentoPacienteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'paciente', 'data_upload')
    list_filter = ('paciente', 'data_upload')
    search_fields = ('titulo', 'descricao', 'paciente__first_name', 'paciente__last_name')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data_horario', 'status')
    list_filter = ('status', 'data_horario', 'medico')
    search_fields = ('paciente__first_name', 'paciente__last_name', 'medico__first_name', 'medico__last_name')
    actions = ['aprovar_consultas', 'negar_consultas']

    def aprovar_consultas(self, _, queryset):
        queryset.update(status='APROVADO')
    aprovar_consultas.short_description = "Aprovar consultas selecionadas"

    def negar_consultas(self, _, queryset):
        queryset.update(status='NEGADO')
    negar_consultas.short_description = "Negar consultas selecionadas"
