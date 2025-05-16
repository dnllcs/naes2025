from django.urls import path

from .views import PedidoCreate, ItemPedidoCreate, AtendenteCreate, TicketSuporteCreate, MensagemAtendimentoCreate


urlpatterns = [
    # CreateView ##########################################################
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/item-pedido/", ItemPedidoCreate.as_view(), name="item-pedido"),
    path("cadastrar/atendente/", AtendenteCreate.as_view(), name="atendente-create"),
    path("cadastrar/ticket-suporte/", TicketSuporteCreate.as_view(), name="cadastrar-ticket-suporte"),
    path("cadastrar/mensagem-atendimento/", MensagemAtendimentoCreate.as_view(), name="cadastrar-mensagem-atendimento"),
]