from django.urls import path

from .views import (ClienteList, ClienteCreate,
ClienteUpdate,
ClienteDelete,
AtendenteList,
AtendenteCreate,
TicketList,
TicketDetail,
TicketCreate,
TicketUpdate,
MensagemCreate,
AvaliacaoCreate)

urlpatterns = [
    path("clientes/", ClienteList.as_view(), name="cliente_list"),
    path("clientes/cadastrar/", ClienteCreate.as_view(), name="cliente_create"),
    path("clientes/<int:pk>/editar/", ClienteUpdate.as_view(), name="cliente_update"),
    path("clientes/<int:pk>/excluir/", ClienteDelete.as_view(), name="cliente_delete"),
    path("atendentes/", AtendenteList.as_view(), name="atendente_list"),
    path("atendentes/cadastrar/", AtendenteCreate.as_view(), name="atendente_create"),
    path("tickets/", TicketList.as_view(), name="ticket_list"),
    path("tickets/<int:pk>/", TicketDetail.as_view(), name="ticket_detail"),
    path("tickets/cadastrar/", TicketCreate.as_view(), name="ticket_create"),
    path("tickets/<int:pk>/editar/", TicketUpdate.as_view(), name="ticket_update"),
    path("mensagens/cadastrar/", MensagemCreate.as_view(), name="mensagem_create"),
    path("avaliacoes/cadastrar/", AvaliacaoCreate.as_view(), name="avaliacao_create"),
]