from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_pendentes_list, name='tarefas_pendentes_list'),
    path('<int:tarefa_id>/concluir/', views.concluir_tarefa, name="concluir_tarefa"),
    path('<int:tarefa_id>/excluir/', views.excluir_tarefa, name="excluir_tarefa"),
    path('<int:tarefa_id>/adiar/', views.adiar_tarefa, name="adiar_tarefa"),
    path('<int:tarefa_id>/editar', views.editar_tarefa, name="editar_tarefa"),
    path('<int:tarefa_id>/mover_para_tarefas', views.mover_para_tarefas, name="mover_para_tarefas"),
    path('concluidas/', views.tarefas_concluidas_list, name="tarefas_concluidas_list"),
    path('adidas/', views.tarefas_adiadas_list, name="tarefas_adiadas_list")
]
