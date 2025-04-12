# Modelagem de Solução com RPA
Automatizar o processo de verificação e envio de documentos para demandas de validação, conforme descrito a seguir:
1. Consumir uma API autenticada que retorna as demandas de validação por CNPJ ou CPF.
2. Verificar o diretório principal de armazenamento por pastas com CNPJs ou CPFs.
3. Identificar se há demandas correspondentes às pastas.
4. Acessar o caminho do diretório indicado pela API.
5. Localizar o arquivo solicitado.
6. Realizar o upload do arquivo via API autenticada.

---
## Arquitetura Da Solução
* <b>Tecnologia sugerida:</b> ***Python*** com biblioteca ***requests*** para consumo de API, os e ***pathlib*** para navegação de diretórios, e tratamento com logs nativos (logging).

* <b>Execução:</b> RPA customizado ou framework como Robot Framework, ***TagUI***, ou ***UiPath*** (com Python).
---
## Estrutura de Pastas
````bash
/RPA_ValidacaoDocumentos
│
├── /scripts
│   └── main.py                    # Script principal da automação
│   └── api_utils.py              # Módulo para autenticação e chamadas API
│   └── file_handler.py           # Funções para navegação e manipulação de arquivos
│
├── /logs
│   └── execucao_2025-04-12.log
│
├── /config
│   └── credentials.json          # Armazenamento seguro de tokens (com criptografia)
│   └── settings.yaml             # Configurações como endpoints, diretórios, etc.
│
└── README.md
````
---
## Segurança e Autenticação
 <b>Autenticação Token/Bearer:</b> A API deve ser acessada via token de autenticação.</b>

* <b>Armazenamento seguro de credenciais:</b> Utilização de .env ou criptografia simétrica (ex: Fernet) para tokens.

* <b>Evitar dados sensíveis no código. Toda configuração deve estar externa.</b>

* <b>Validação de pastas:</b> Aplicar regex para garantir que a pasta corresponde a um CNPJ ou CPF válido.
---
## Fluxo de Automação
1. **Autenticação na API**
   - Solicita token JWT ou Bearer.
   - Armazena apenas em memória ou criptografado.

2. **Consulta de demandas**
   - Exemplo de retorno:
     ```json
     [
       {
         "documento": "12345678000199",
         "tipo": "CNPJ",
         "path_destino": "/clientes/12345678000199/",
         "nome_arquivo": "comprovante.pdf"
       }
     ]
     ```

3. **Busca de pastas**
   - Percorre diretório principal (`/clientes`) em busca de nomes que batam com os documentos da API.

4. **Verificação de demanda**
   - Confirma se há match entre pasta local e demandas.

5. **Upload de arquivos**
   - Valida o nome do arquivo solicitado e faz upload:
     ```
     POST /api/upload
     Headers: Authorization: Bearer <token>
     Body: multipart/form-data (arquivo)
     ```

6. **Logs**
   - Armazena todas as ações em `/logs/execucao_<data>.log`.

---
## Boas Práticas
- Modularização por responsabilidade (API, arquivos, log).
- Separação de variáveis sensíveis em `.env` ou `settings.yaml`.
- Retentativas automáticas em caso de falha na API.
- Uso de `logging` Python com níveis INFO, WARNING, ERROR.
- Geração de alertas para falhas críticas (via log, e-mail ou webhook).

---
## Requisitos Técnicos

- Python 3.8+
- Bibliotecas sugeridas:
  - `requests`, `python-dotenv`, `pyyaml`, `cryptography`, `logging`, `re`, `os`, `pathlib`
