from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import (
    Cliente, Atendente, Ticket, CategoriaTicket,
    StatusTicket, Mensagem, AvaliacaoAtendimento,
    Estado, HistoricoStatus
)
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Cliente
    fields = ["nome", "email", "telefone", "cidade", "estado"]
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Cadastro de Cliente"}

class AtendenteCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Atendente
    fields = ["nome", "email", "telefone", "departamento", "data_contratacao"]
    success_url = reverse_lazy("atendente_list")
    extra_context = {"titulo": "Cadastro de Atendente"}

class TicketCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Ticket
    fields = ["cliente", "atendente_responsavel", "categoria",
              "status_atual", "titulo", "descricao", "prioridade"]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Abrir Novo Ticket"}

class CategoriaTicketCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = CategoriaTicket
    fields = ["nome", "descricao"]
    success_url = reverse_lazy("categoria_ticket_list")
    extra_context = {"titulo": "Cadastrar Categoria de Ticket"}

class StatusTicketCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = StatusTicket
    fields = ["nome"]
    success_url = reverse_lazy("status_ticket_list")
    extra_context = {"titulo": "Cadastrar Status de Ticket"}

class MensagemCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Mensagem
    fields = ["ticket", "autor_cliente", "autor_atendente", "conteudo"]
    success_url = reverse_lazy("mensagem_list")
    extra_context = {"titulo": "Nova Mensagem no Ticket"}

class AvaliacaoCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = AvaliacaoAtendimento
    fields = ["ticket", "nota", "comentario"]
    success_url = reverse_lazy("avaliacao_list")
    extra_context = {"titulo": "Avaliar Atendimento"}

class EstadoCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Estado
    fields = ["nome", "sigla"]
    success_url = reverse_lazy("estado_list")
    extra_context = {"titulo": "Cadastrar Estado"}

class HistoricoStatusCreate(CreateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = HistoricoStatus
    fields = ["ticket", "status", "alterado_por"]
    success_url = reverse_lazy("historico_status_list")
    extra_context = {"titulo": "Registrar Mudança de Status"}




class ClienteList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/cliente_list.html"
    model = Cliente
    context_object_name = "clientes"
    paginate_by = 20

class AtendenteList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/atendente_list.html"
    model = Atendente
    context_object_name = "atendentes"
    paginate_by = 20

class TicketList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/ticket_list.html"
    model = Ticket
    context_object_name = "tickets"
    paginate_by = 20

class CategoriaTicketList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/categoria_ticket_list.html"
    model = CategoriaTicket
    context_object_name = "categorias"
    paginate_by = 20

class StatusTicketList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/status_ticket_list.html"
    model = StatusTicket
    context_object_name = "statuses"
    paginate_by = 20

class MensagemList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/mensagem_list.html"
    model = Mensagem
    context_object_name = "mensagens"
    paginate_by = 20

class AvaliacaoList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/avaliacao_list.html"
    model = AvaliacaoAtendimento
    context_object_name = "avaliacoes"
    paginate_by = 20

class EstadoList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/estado_list.html"
    model = Estado
    context_object_name = "estados"
    paginate_by = 20

class HistoricoStatusList(ListView, LoginRequiredMixin):
    template_name = "suporte/listas/historico_status_list.html"
    model = HistoricoStatus
    context_object_name = "historicos"
    paginate_by = 20




class ClienteUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Cliente
    fields = ["nome", "email", "telefone", "cidade", "estado"]
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Atualizar Cliente"}

class AtendenteUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Atendente
    fields = ["nome", "email", "telefone", "departamento", "data_contratacao"]
    success_url = reverse_lazy("atendente_list")
    extra_context = {"titulo": "Atualizar Atendente"}

class TicketUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Ticket
    fields = ["cliente", "atendente_responsavel", "categoria",
              "status_atual", "titulo", "descricao", "prioridade"]
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Atualizar Ticket"}

class CategoriaTicketUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = CategoriaTicket
    fields = ["nome", "descricao"]
    success_url = reverse_lazy("categoria_ticket_list")
    extra_context = {"titulo": "Atualizar Categoria de Ticket"}

class StatusTicketUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = StatusTicket
    fields = ["nome"]
    success_url = reverse_lazy("status_ticket_list")
    extra_context = {"titulo": "Atualizar Status de Ticket"}

class MensagemUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Mensagem
    fields = ["ticket", "autor_cliente", "autor_atendente", "conteudo"]
    success_url = reverse_lazy("mensagem_list")
    extra_context = {"titulo": "Atualizar Mensagem"}

class AvaliacaoUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = AvaliacaoAtendimento
    fields = ["ticket", "nota", "comentario"]
    success_url = reverse_lazy("avaliacao_list")
    extra_context = {"titulo": "Atualizar Avaliação"}

class EstadoUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = Estado
    fields = ["nome", "sigla"]
    success_url = reverse_lazy("estado_list")
    extra_context = {"titulo": "Atualizar Estado"}

class HistoricoStatusUpdate(UpdateView, LoginRequiredMixin):
    template_name = "suporte/form.html"
    model = HistoricoStatus
    fields = ["ticket", "status", "alterado_por"]
    success_url = reverse_lazy("historico_status_list")
    extra_context = {"titulo": "Atualizar Histórico de Status"}




class ClienteDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = Cliente
    success_url = reverse_lazy("cliente_list")
    extra_context = {"titulo": "Excluir Cliente"}

class AtendenteDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = Atendente
    success_url = reverse_lazy("atendente_list")
    extra_context = {"titulo": "Excluir Atendente"}

class TicketDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = Ticket
    success_url = reverse_lazy("ticket_list")
    extra_context = {"titulo": "Excluir Ticket"}

class CategoriaTicketDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = CategoriaTicket
    success_url = reverse_lazy("categoria_ticket_list")
    extra_context = {"titulo": "Excluir Categoria de Ticket"}

class StatusTicketDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = StatusTicket
    success_url = reverse_lazy("status_ticket_list")
    extra_context = {"titulo": "Excluir Status de Ticket"}

class MensagemDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = Mensagem
    success_url = reverse_lazy("mensagem_list")
    extra_context = {"titulo": "Excluir Mensagem"}

class AvaliacaoDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = AvaliacaoAtendimento
    success_url = reverse_lazy("avaliacao_list")
    extra_context = {"titulo": "Excluir Avaliação"}

class EstadoDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = Estado
    success_url = reverse_lazy("estado_list")
    extra_context = {"titulo": "Excluir Estado"}

class HistoricoStatusDelete(DeleteView, LoginRequiredMixin):
    template_name = "suporte/confirm_delete.html"
    model = HistoricoStatus
    success_url = reverse_lazy("historico_list")
    extra_context = {"titulo": "Excluir Histórico de Status"}