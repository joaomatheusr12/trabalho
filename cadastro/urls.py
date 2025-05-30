from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
    path('criar/', views.criar_pessoa, name='criar_pessoa'),
    path('detalhes/<int:pessoa_id>/', views.detalhes_pessoa, name='detalhes_pessoa'),
]
