from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarefa
from .forms import TarefaForm

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefas/list.html'
    context_object_name = 'tarefas'
    paginate_by = 10

class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefas/form.html'
    success_url = reverse_lazy('lista-tarefas')

class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefas/form.html'
    success_url = reverse_lazy('lista-tarefas')

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'tarefas/confirm_delete.html'
    success_url = reverse_lazy('lista-tarefas')