from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.sigla

    class Meta:
        ordering = ['nome']


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Atendente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    departamento = models.CharField(max_length=100, blank=True)
    data_contratacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class CategoriaTicket(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class StatusTicket(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Ticket(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    atendente_responsavel = models.ForeignKey(
        Atendente, on_delete=models.SET_NULL, null=True, blank=True
    )
    categoria = models.ForeignKey(CategoriaTicket, on_delete=models.PROTECT)
    status_atual = models.ForeignKey(StatusTicket, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Ticket #{self.pk} - {self.titulo}'

    class Meta:
        ordering = ['-data_abertura']


class Mensagem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="mensagens")
    autor_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    autor_atendente = models.ForeignKey(Atendente, on_delete=models.SET_NULL, null=True, blank=True)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem #{self.pk} - Ticket {self.ticket.pk}'

    class Meta:
        ordering = ['data_envio']


class AvaliacaoAtendimento(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    nota = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação Ticket #{self.ticket.pk} - Nota {self.nota}'


class HistoricoStatus(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="historico_status")
    status = models.ForeignKey(StatusTicket, on_delete=models.PROTECT)
    alterado_por = models.ForeignKey(Atendente, on_delete=models.SET_NULL, null=True)
    data_alteracao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Histórico #{self.pk} - Ticket {self.ticket.pk} [{self.status}]'

    class Meta:
        ordering = ['-data_alteracao']