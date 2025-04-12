from django.contrib import admin
from .models import  Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'inicio', 'termino')
    list_filter = ('status', 'prioridade')
    search_fields = ('titulo',)
    ordering = ('inicio',)
