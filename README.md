# desafio_b2b_python

Projeto desenvolvido para o desafio técnico da b2bflow.

O objetivo é buscar contatos cadastrados no Supabase e enviar uma mensagem personalizada para até 3 contatos utilizando a Z-API.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Configuração da tabela

Tabela: `contatos`

Campos:

* id
* nome
* telefone

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Executando

```bash
python main.py
```

## O que o projeto faz

* Busca os contatos no Supabase
* Limita o envio para até 3 registros
* Monta a mensagem com o nome do contato
* Envia a mensagem pela Z-API
* Exibe informações de sucesso ou erro no terminal

```
```
