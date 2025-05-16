from django.shortcuts import render
from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "User"
        return context


