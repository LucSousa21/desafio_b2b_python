# Desafio b2bflow - Integração Supabase + Z-API

Projeto desenvolvido para o desafio técnico da b2bflow.

A aplicação busca contatos cadastrados em um banco no Supabase e envia uma mensagem personalizada via Z-API para até 3 contatos.

---

## Como funciona

O fluxo do projeto é simples:

1. Busca contatos no Supabase
2. Limita o retorno a 3 registros
3. Monta uma mensagem personalizada com o nome do contato
4. Envia a mensagem via Z-API

---

## Mensagem enviada

```text
Olá, <nome_contato>, tudo bem com você?