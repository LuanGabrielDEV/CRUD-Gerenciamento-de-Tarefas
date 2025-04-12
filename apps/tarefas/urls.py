from django.urls import path
from .views import TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView

urlpatterns = [
    path('', TarefaListView.as_view(), name='lista-tarefas'),
    path('nova/', TarefaCreateView.as_view(), name='criar-tarefa'),
    path('<int:pk>/editar/', TarefaUpdateView.as_view(), name='editar-tarefa'),
    path('<int:pk>/excluir/', TarefaDeleteView.as_view(), name='excluir-tarefa'),
]
