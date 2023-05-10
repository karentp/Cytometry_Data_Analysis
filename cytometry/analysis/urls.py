from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plot_1/', views.plot_1, name='plot_1')
]
