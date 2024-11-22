from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:post_id>', views.post, name="post"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('mensagens/', views.mensagem, name="mensagem"),
    path('mensagens/<int:mensagem_id>/editar', views.editar_mensagem, name="editar_mensagem"),
]
