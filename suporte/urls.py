from django.urls import path

from .views import PedidoCreate, ItemPedidoCreate, AtendenteCreate, TicketSuporteCreate, MensagemAtendimentoCreate
from .views import PedidoUpdate, ItemPedidoUpdate, AtendenteUpdate, TicketSuporteUpdate, MensagemAtendimentoUpdate


urlpatterns = [
    # CreateView ##########################################################
    path("cadastrar/pedido/", PedidoCreate.as_view(), name="cadastrar-pedido"),
    path("cadastrar/item-pedido/", ItemPedidoCreate.as_view(), name="cadastrar-item-pedido"),
    path("cadastrar/atendente/", AtendenteCreate.as_view(), name="cadastrar-atendente-create"),
    path("cadastrar/ticket-suporte/", TicketSuporteCreate.as_view(), name="cadastrar-ticket-suporte"),
    path("cadastrar/mensagem-atendimento/", MensagemAtendimentoCreate.as_view(), name="cadastrar-mensagem-atendimento"),
    
    path("editar/pedido/", PedidoUpdate.as_view(), name="editar-pedido"),
    path("editar/item-pedido/", ItemPedidoUpdate.as_view(), name="editar-item-pedido"),
    path("editar/atendente/", AtendenteUpdate.as_view(), name="editar-atendente-create"),
    path("editar/ticket-suporte/", TicketSuporteUpdate.as_view(), name="editar-ticket-suporte"),
    path("editar/mensagem-atendimento/", MensagemAtendimentoUpdate.as_view(), name="editar-mensagem-atendimento"),
    
    path("", PedidoCreate.as_view(), name="index"),

]