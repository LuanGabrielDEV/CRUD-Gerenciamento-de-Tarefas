from django.db import models

class Tarefa(models.Model):
    PRIORIDADES = [('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')]
    STATUS = [('pendente', 'Pendente'), ('concluido', 'Concluído'), ('atrasado', 'Atrasado')]

    titulo = models.CharField(max_length=100)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES)
    status = models.CharField(max_length=10, choices=STATUS)
    repetir = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return (
        f"Título: {self.titulo} | "
        f"Início: {self.inicio.strftime('%d/%m/%Y %H:%M')} | "
        f"Término: {self.termino.strftime('%d/%m/%Y %H:%M')} | "
        f"Prioridade: {self.get_prioridade_display()} | "
        f"Status: {self.get_status_display()} | "
        f"Repetir: {self.repetir if self.repetir else 'Não se repete'}"
    )
