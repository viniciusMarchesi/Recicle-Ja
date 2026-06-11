from django.db import models

class Material(models.Model):
    nome = models.CharField("Nome do Material", max_length=100, unique=True)
    slug = models.SlugField("Slug", unique=True, max_length=100)
    instrucoes_preparo = models.TextField("Instruções de Preparo")
    icone = models.CharField("Ícone (Bootstrap Icons)", max_length=50, blank=True, help_text="Ex: bi-recycle, bi-box, bi-droplet")

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class PontoDeColeta(models.Model):
    nome = models.CharField("Nome do Ecoponto", max_length=150)
    endereco = models.CharField("Endereço Completo", max_length=255)
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6)
    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6)
    materiais_aceitos = models.ManyToManyField(Material, related_name="pontos_coleta", verbose_name="Materiais Aceitos")
    
    STATUS_CHOICES = [
        ("Ativo", "Ativo"),
        ("Indisponível", "Indisponível"),
        ("Em manutenção", "Em manutenção"),
    ]
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="Ativo")
    horario_funcionamento = models.CharField("Horário de Funcionamento", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Ponto de Coleta"
        verbose_name_plural = "Pontos de Coleta"
        ordering = ['nome']

    def __str__(self):
        return self.nome



class Feedback(models.Model):
    TIPO_CHOICES = [
        ('sugestao', 'Sugestão de Novo Ponto'),
        ('manutencao', 'Relato de Problema/Manutenção'),
        ('outro', 'Outros Assuntos'),
    ]

    nome = models.CharField("Nome (opcional)", max_length=100, blank=True)
    email = models.EmailField("E-mail (opcional)", blank=True)
    tipo_feedback = models.CharField("Tipo de Feedback", max_length=20, choices=TIPO_CHOICES, default='sugestao')
    ponto_coleta = models.ForeignKey(
        PontoDeColeta, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="feedbacks",
        verbose_name="Ponto de Coleta Referente"
    )
    mensagem = models.TextField("Mensagem")
    lido = models.BooleanField("Lido/Revisado", default=False)
    criado_em = models.DateTimeField("Enviado em", auto_now_add=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        ordering = ['-criado_em']

    def __str__(self):
        tipo_str = dict(self.TIPO_CHOICES).get(self.tipo_feedback, self.tipo_feedback)
        return f"{tipo_str} - {self.nome or 'Anônimo'}"



class LocalDeDescarte(models.Model):
    nome = models.CharField(max_length=150)  # Ex: "Caçamba 1"
    descricao = models.TextField(blank=True)  # Informações extras
    ponto_coleta = models.ForeignKey(PontoDeColeta, on_delete=models.CASCADE, related_name="locais_descarte")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="locais_descarte")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.material.nome} ({self.ponto_coleta.nome})"
