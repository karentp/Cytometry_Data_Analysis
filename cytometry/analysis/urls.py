# analysis/urls.py

from django.urls import path
from . import views  # Import aus demselben Verzeichnis

urlpatterns = [
    path('', views.home, name='home'),
    path('plot_histogram/<int:file_id>/', views.plot_histogram, name='plot_histogram'),
    path('plot_dot/<int:file_id>/', views.plot_dot, name='plot_dot'),
    path('plot_density/<int:file_id>/', views.plot_density, name='plot_density'),
    path('plot_time/<int:file_id>/', views.plot_time, name='plot_time'),
    # ... Weitere URL-Pfade für Ihre Ansichten ...
]
