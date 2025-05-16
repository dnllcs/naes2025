from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Pedido, ItemPedido, Atendente, TicketSuporte, MensagemAtendimento

class PedidoCreate(CreateView):
    template_name = "suporte/form.html"
    model = Pedido
    success_url = reverse_lazy("index")
    fields = ["usuario", "data_pedido", "status_pedido"]
    extra_context = {
        "titulo": "Cadastro de Pedido"
    }

class ItemPedidoCreate(CreateView):
    template_name = "suporte/form.html"
    model = ItemPedido
    success_url = reverse_lazy("index")
    fields = ["pedido", "nome_item", "quantidade"]
    extra_context = {
        "titulo": "Cadastro de Item do Pedido"
    }

class AtendenteCreate(CreateView):
    template_name = "suporte/form.html"
    model = Atendente
    success_url = reverse_lazy("index")
    fields = ["nome", "email", "senha"]
    extra_context = {
        "titulo": "Cadastro de Atendente"
    }

class TicketSuporteCreate(CreateView):
    template_name = "suporte/form.html"
    model = TicketSuporte
    success_url = reverse_lazy("index")
    fields = [
        "usuario",
        "pedido",
        "item_pedido",
        "atendente",
        "tipo_ticket",
        "status_ticket",
        "descricao_problema",
        "data_fechamento"
    ]
    extra_context = {
        "titulo": "Cadastro de Ticket de Suporte"
    }

class MensagemAtendimentoCreate(CreateView):
    template_name = "suporte/form.html"
    model = MensagemAtendimento
    success_url = reverse_lazy("index")
    fields = ["ticket", "usuario", "mensagem"]
    extra_context = {
        "titulo": "Cadastro de Mensagem de Atendimento"
    }
