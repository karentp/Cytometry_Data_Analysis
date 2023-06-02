from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import PieDePagina

# Create your views here.
class HomePageView(TemplateView):
    template_name ="frontend/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pieDePagina"] = PieDePagina.objects.all()
        context["title"] = "Titulo Pagina"
        return context