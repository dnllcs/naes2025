from django.urls import path
from .views import (
    ClienteCreate, ClienteList, ClienteUpdate, ClienteDelete,
    AtendenteCreate, AtendenteList, AtendenteUpdate, AtendenteDelete,
    TicketCreate, TicketList, TicketUpdate, TicketDelete,
    CategoriaTicketCreate, CategoriaTicketList, CategoriaTicketUpdate, CategoriaTicketDelete,
    StatusTicketCreate, StatusTicketList, StatusTicketUpdate, StatusTicketDelete,
    MensagemCreate, MensagemList, MensagemUpdate, MensagemDelete,
    AvaliacaoCreate, AvaliacaoList, AvaliacaoUpdate, AvaliacaoDelete,
    EstadoCreate, EstadoList, EstadoUpdate, EstadoDelete,
    HistoricoStatusCreate, HistoricoStatusList, HistoricoStatusUpdate, HistoricoStatusDelete,
)

urlpatterns = [
    path("clientes/", ClienteList.as_view(), name="cliente_list"),
    path("clientes/cadastrar/", ClienteCreate.as_view(), name="cliente_create"),
    path("clientes/<int:pk>/editar/", ClienteUpdate.as_view(), name="cliente_update"),
    path("clientes/<int:pk>/excluir/", ClienteDelete.as_view(), name="cliente_delete"),

    path("atendentes/", AtendenteList.as_view(), name="atendente_list"),
    path("atendentes/cadastrar/", AtendenteCreate.as_view(), name="atendente_create"),
    path("atendentes/<int:pk>/editar/", AtendenteUpdate.as_view(), name="atendente_update"),
    path("atendentes/<int:pk>/excluir/", AtendenteDelete.as_view(), name="atendente_delete"),

    path("tickets/", TicketList.as_view(), name="ticket_list"),
    path("tickets/cadastrar/", TicketCreate.as_view(), name="ticket_create"),
    path("tickets/<int:pk>/editar/", TicketUpdate.as_view(), name="ticket_update"),
    path("tickets/<int:pk>/excluir/", TicketDelete.as_view(), name="ticket_delete"),

    path("categorias/", CategoriaTicketList.as_view(), name="categoria_ticket_list"),
    path("categorias/cadastrar/", CategoriaTicketCreate.as_view(), name="categoria_ticket_create"),
    path("categorias/<int:pk>/editar/", CategoriaTicketUpdate.as_view(), name="categoria_ticket_update"),
    path("categorias/<int:pk>/excluir/", CategoriaTicketDelete.as_view(), name="categoria_ticket_delete"),

    path("statuses/", StatusTicketList.as_view(), name="status_ticket_list"),
    path("statuses/cadastrar/", StatusTicketCreate.as_view(), name="status_ticket_create"),
    path("statuses/<int:pk>/editar/", StatusTicketUpdate.as_view(), name="status_ticket_update"),
    path("statuses/<int:pk>/excluir/", StatusTicketDelete.as_view(), name="status_ticket_delete"),

    path("mensagens/", MensagemList.as_view(), name="mensagem_list"),
    path("mensagens/cadastrar/", MensagemCreate.as_view(), name="mensagem_create"),
    path("mensagens/<int:pk>/editar/", MensagemUpdate.as_view(), name="mensagem_update"),
    path("mensagens/<int:pk>/excluir/", MensagemDelete.as_view(), name="mensagem_delete"),

    path("avaliacoes/", AvaliacaoList.as_view(), name="avaliacao_list"),
    path("avaliacoes/cadastrar/", AvaliacaoCreate.as_view(), name="avaliacao_create"),
    path("avaliacoes/<int:pk>/editar/", AvaliacaoUpdate.as_view(), name="avaliacao_update"),
    path("avaliacoes/<int:pk>/excluir/", AvaliacaoDelete.as_view(), name="avaliacao_delete"),

    path("estados/", EstadoList.as_view(), name="estado_list"),
    path("estados/cadastrar/", EstadoCreate.as_view(), name="estado_create"),
    path("estados/<int:pk>/editar/", EstadoUpdate.as_view(), name="estado_update"),
    path("estados/<int:pk>/excluir/", EstadoDelete.as_view(), name="estado_delete"),

    path("historicos/", HistoricoStatusList.as_view(), name="historico_status_list"),
    path("historicos/cadastrar/", HistoricoStatusCreate.as_view(), name="historico_status_create"),
    path("historicos/<int:pk>/editar/", HistoricoStatusUpdate.as_view(), name="historico_status_update"),
    path("historicos/<int:pk>/excluir/", HistoricoStatusDelete.as_view(), name="historico_status_delete"),
]