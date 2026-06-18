# Desafio Técnico b2bflow - Integração Supabase + Z-API

Script em Python desenvolvido para o desafio de estágio da b2bflow. A aplicação faz a leitura de contatos cadastrados em um banco de dados no Supabase e dispara uma mensagem personalizada para o WhatsApp deles via Z-API, limitando o fluxo a no máximo 3 contatos.

## Como o script funciona

1. Executa uma query no Supabase buscando os registros da tabela de contatos.
2. Limita o retorno em até 3 linhas (conforme regra do desafio).
3. Percorre os resultados montando a string exata solicitada.
4. Faz um disparo via requisição POST para a API da Z-API para cada número.

---

## Estrutura do Banco (Supabase)

Para que o script funcione, a tabela no Supabase foi criada com o nome `contatos` contendo os seguintes campos:

* `id`: int8 (Primary Key)
* `nome`: varchar (Nome do cliente/contato)
* `telefone`: varchar (Número com DDD, ex: `5511999999999`)

---

## Configuração do Ambiente (.env)

Crie um arquivo chamado `.env` na raiz do projeto (use o `.env.example` como base) e preencha com as suas chaves:

```env
SUPABASE_URL=seu_supabase_url_aqui
SUPABASE_ANON_KEY=sua_supabase_anon_key_aqui
ZAPI_INSTANCE_ID=seu_id_da_instancia_aqui
ZAPI_TOKEN=seu_token_da_instancia_aqui

```

---

## Como rodar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/LucSousa21/desafio_b2b_python.git
cd nome-do-repositorio

```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt

```

3. **Execute o script principal:**

```bash
python main.py

```

---

*Desenvolvido por Lucas para o processo seletivo da b2bflow.*