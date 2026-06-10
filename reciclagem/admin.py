from django.contrib import admin
from .models import Material, PontoDeColeta, Feedback, LocalDeDescarte

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'icone')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome',)

@admin.register(PontoDeColeta)
class PontoDeColetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'latitude', 'longitude', 'ativo')
    list_filter = ('ativo', 'materiais_aceitos')
    search_fields = ('nome', 'endereco')
    filter_horizontal = ('materiais_aceitos',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('tipo_feedback', 'nome', 'email', 'ponto_coleta', 'lido', 'criado_em')
    list_filter = ('lido', 'tipo_feedback', 'criado_em')
    search_fields = ('nome', 'email', 'mensagem')
    readonly_fields = ('criado_em',)
    actions = ['marcar_como_lido']

    def marcar_como_lido(self, request, queryset):
        queryset.update(lido=True)
        self.message_user(request, "Feedbacks selecionados foram marcados como lidos.")
    marcar_como_lido.short_description = "Marcar como lidos"

@admin.register(LocalDeDescarte)
class LocalDeDescarteAdmin(admin.ModelAdmin):
    list_display = ("nome", "material", "ponto_coleta", "ativo")
    list_filter = ("material", "ponto_coleta", "ativo")
    search_fields = ("nome", "descricao")

