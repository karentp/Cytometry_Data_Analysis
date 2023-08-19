from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact(request):
    contact_form = ContactForm()
    return render(request, "contact/contact.html", {'form' : contact_form })