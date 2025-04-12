# Projeto Django - Gerenciamento de Tarefas

Este é um projeto Django para gerenciamento de tarefas, permitindo aos usuários criar, editar, excluir e listar tarefas. O projeto utiliza funcionalidades básicas de CRUD (Create, Read, Update, Delete) e inclui a página de administração do Django para gerenciar os dados.

## Funcionalidades

- **Listagem de Tarefas**: Visualização de todas as tarefas armazenadas no banco de dados.
- **Criação de Tarefas**: Adicionar novas tarefas com informações como título, data de início e término, prioridade, status e repetição.
- **Edição de Tarefas**: Atualizar informações de tarefas existentes.
- **Exclusão de Tarefas**: Remover tarefas do banco de dados.
- **Administração**: Acesso à interface administrativa do Django para gerenciar tarefas.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- **Python 3.8+**: O projeto foi desenvolvido com Python 3.8 e versões superiores.
- **pip**: O gerenciador de pacotes do Python.

Se o Python não estiver instalado em sua máquina, baixe e instale a versão mais recente [aqui](https://www.python.org/downloads/).

## Como Rodar o Projeto

### 1. Clonar o Repositório

Clone o repositório do projeto:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar o Django e Dependências
Passo 1: Criar um Ambiente Virtual
Para isolar as dependências do projeto, é recomendado criar um ambiente virtual:

````bash
python -m venv venv
````
Ative o ambiente virtual:

No Windows:

````bash
venv\Scripts\activate
````
No macOS/Linux:
````bash
source venv/bin/activate
````
### Passo 2: Instalar o Django
Com o ambiente virtual ativo, instale o Django e outras dependências:

````bash
pip install django
````
O projeto já possui um arquivo requirements.txt com as dependências, instale todas as dependências com:

````bash
pip install -r requirements.txt
````
### 3. Configuração do Banco de Dados
### Passo 1: Verificar Configuração do Banco de Dados
Por padrão, o Django usa o banco de dados SQLite, que é um banco de dados leve e embutido. A configuração no arquivo settings.py deve ser semelhante a esta:

````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
````
Essa configuração cria um banco de dados local no arquivo db.sqlite3 no diretório raiz do projeto.

### Passo 2: Criar as Tabelas no Banco de Dados
Com a configuração do banco de dados verificada, agora você precisa criar as tabelas no banco de dados. Execute o seguinte comando para aplicar as migrações:

````bash
python manage.py migrate
Este comando criará as tabelas necessárias para o projeto, incluindo o modelo Tarefa.
````
### 4. Criar um Superusuário (Opcional)
Se você deseja acessar a interface administrativa do Django, será necessário criar um superusuário. Execute o seguinte comando:

````bash
python manage.py createsuperuser
Siga as instruções para fornecer um nome de usuário, e-mail e senha para o superusuário.
````

### 5. Rodar o Servidor de Desenvolvimento
Após aplicar as migrações e, opcionalmente, criar o superusuário, inicie o servidor de desenvolvimento do Django com:

````bash
python manage.py runserver
````
O servidor será iniciado na URL http://127.0.0.1:8000/. Abra seu navegador e acesse essa URL para visualizar o projeto.

### 6. Popular o Banco de Dados 
Existem duas formas principais para popular o banco de dados com dados de exemplo:

- Método 1: Usando o Admin do Django
Inicie o servidor de desenvolvimento com o comando python manage.py runserver.

Acesse o painel administrativo do Django em http://127.0.0.1:8000/admin/.

Faça login com o superusuário criado anteriormente.

No painel administrativo, você pode adicionar ou editar tarefas manualmente.

-  Método 2: Usando o Shell do Django
Caso deseje adicionar dados diretamente via terminal, você pode usar o shell do Django:

````bash

python manage.py shell
````
Dentro do shell, você pode criar uma tarefa como exemplo:

````python

from tarefas.models import Tarefa
from django.utils import timezone
````

# Criando uma tarefa de exemplo
````
tarefa = Tarefa.objects.create(
    titulo='Tarefa de Exemplo',
    inicio=timezone.now(),
    termino=timezone.now() + timezone.timedelta(hours=1),
    prioridade='media',
    status='pendente',
    repetir='diariamente'
)
tarefa.save()
````
### 7. Acessar o Projeto
Após seguir todos os passos, você pode acessar seu projeto Django localmente através do navegador em:
````cpp
http://127.0.0.1:8000/
````
Na interface, você poderá interagir com as tarefas e utilizar as funcionalidades de criação, edição e exclusão
