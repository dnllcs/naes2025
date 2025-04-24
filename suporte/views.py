from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "suporte/index.html"
    
# Create your views here.
