from django.contrib import admin
from .models import Pedido, ItemPedido, Atendente, TicketSuporte, MensagemAtendimento

admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Atendente)
admin.site.register(TicketSuporte)
admin.site.register(MensagemAtendimento)

# Register your models here.
