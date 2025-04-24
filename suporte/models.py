from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_pedido = models.DateTimeField()
    status_pedido = models.CharField(max_length=50)

    def __str__(self):
        return f'Pedido #{self.id} - {self.usuario.username}'

    class Meta:
        ordering = ['-data_pedido']


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nome_item = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome_item} x{self.quantidade} - Pedido #{self.pedido.id}'

    class Meta:
        ordering = ['pedido']


class Atendente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class TicketSuporte(models.Model):
    TIPO_CHOICES = [
        ('devolucao', 'Devolução'),
        ('troca', 'Troca'),
        ('reclamacao', 'Reclamação'),
        ('duvida', 'Dúvida'),
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em Andamento'),
        ('resolvido', 'Resolvido'),
        ('fechado', 'Fechado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    pedido = models.ForeignKey(
        Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    item_pedido = models.ForeignKey(
        ItemPedido, on_delete=models.SET_NULL, null=True, blank=True)
    atendente = models.ForeignKey(
        Atendente, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_ticket = models.CharField(max_length=20, choices=TIPO_CHOICES)
    status_ticket = models.CharField(max_length=20, choices=STATUS_CHOICES)
    descricao_problema = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Ticket #{self.id} - {self.usuario.username} - {self.tipo_ticket}'

    class Meta:
        ordering = ['-data_abertura']
        verbose_name = 'Ticket de Suporte'
        verbose_name_plural = 'Tickets de Suporte'


class MensagemAtendimento(models.Model):
    ticket = models.ForeignKey(TicketSuporte, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem #{self.id} - Ticket #{self.ticket.id}'

    class Meta:
        ordering = ['data_envio']
