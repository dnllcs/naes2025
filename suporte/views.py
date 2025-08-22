from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    Cliente, Atendente, Ticket, CategoriaTicket,
    StatusTicket, Mensagem, AvaliacaoAtendimento, HistoricoStatus
)

class ClienteList(ListView):
    template_name = "suporte/cliente_list.html"
    model = Cliente
    context_object_name = "clientes"

class ClienteCreate(CreateView):
    template_name = "suporte/form.html"
    model = Cliente
    fields = ["nome", "email", "telefone", "cidade", "estado"]
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Cadastro de Cliente"}

class ClienteUpdate(UpdateView):
    template_name = "suporte/form.html"
    model = Cliente
    fields = ["nome", "email", "telefone", "cidade", "estado"]
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Atualizar Cliente"}

class ClienteDelete(DeleteView):
    template_name = "suporte/confirm_delete.html"
    model = Cliente
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Excluir Cliente"}

class AtendenteList(ListView):
    template_name = "suporte/atendente_list.html"
    model = Atendente
    context_object_name = "atendentes"

class AtendenteCreate(CreateView):
    template_name = "suporte/form.html"
    model = Atendente
    fields = ["nome", "email", "telefone", "departamento", "data_contratacao"]
    success_url = reverse_lazy("atendente_list")
    extra_context = {"titulo": "Cadastro de Atendente"}

class TicketList(ListView):
    template_name = "suporte/ticket_list.html"
    model = Ticket
    context_object_name = "tickets"


class TicketDetail(DetailView):
    template_name = "suporte/ticket_detail.html"
    model = Ticket
    context_object_name = "ticket"


class TicketCreate(CreateView):
    template_name = "suporte/form.html"
    model = Ticket
    fields = [
        "cliente", "atendente_responsavel", "categoria",
        "status_atual", "titulo", "descricao", "prioridade"
    ]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Abrir Novo Ticket"}

class TicketUpdate(UpdateView):
    template_name = "suporte/form.html"
    model = Ticket
    fields = [
        "atendente_responsavel", "categoria",
        "status_atual", "titulo", "descricao", "prioridade"
    ]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Atualizar Ticket"}

class MensagemCreate(CreateView):
    template_name = "suporte/form.html"
    model = Mensagem
    fields = ["ticket", "autor_cliente", "autor_atendente", "conteudo"]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Nova Mensagem"}

class AvaliacaoCreate(CreateView):
    template_name = "suporte/form.html"
    model = AvaliacaoAtendimento
    fields = ["ticket", "nota", "comentario"]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Avaliar Atendimento"}
