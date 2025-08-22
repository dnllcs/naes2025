from django.contrib import admin
from .models import Estado, Cliente, Atendente, CategoriaTicket, StatusTicket, Ticket, Mensagem, AvaliacaoAtendimento, HistoricoStatus

admin.site.register(Estado)
admin.site.register(Cliente)
admin.site.register(Atendente)
admin.site.register(CategoriaTicket)
admin.site.register(StatusTicket)
admin.site.register(Ticket)
admin.site.register(Mensagem)
admin.site.register(AvaliacaoAtendimento)
admin.site.register(HistoricoStatus)