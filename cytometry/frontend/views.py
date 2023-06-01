from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name ="frontend/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Titulo Pagina"
        return context