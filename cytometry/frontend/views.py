from .models import SliderImage, PieDePagina, Colaborador, Textos
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "frontend/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slider_images"] = SliderImage.objects.all()
        context["pieDePagina"] = PieDePagina.objects.all()
        context["title"] = "Titulo Pagina"
        context["colaboradores"] = Colaborador.objects.all()
        context["secciones"] = Textos.objects.all()  
        
        return context

