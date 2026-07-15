# apps/empresas/urls.py
from django.urls import path
from . import views

app_name = 'empresas'

urlpatterns = [
    path('', views.empresa_lista, name='lista'),
    path('nova/', views.empresa_criar_view, name='criar'),
    path('editar/<uuid:pk>/', views.empresa_editar_view, name='editar'),
    path('desativar/<uuid:pk>/', views.empresa_desativar_view, name='desativar'),
]