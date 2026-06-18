import os
import requests
from conect_supabase import get_supabase_client

# Função para enviar mensagem usando a API do ZAPI
def enviar_mensagem(nome, telefone):
    try:

        # Carregar variáveis de ambiente
        instance_id = os.getenv("ZAPI_INSTANCE_ID")
        token = os.getenv("ZAPI_TOKEN")

        # Construir a URL da API
        url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
        
        # Mensagem personalizada
        payload = {
            "phone": telefone,
            "message": f"Olá {nome}, tudo bem?"
        }

        # Enviar a requisição POST para a API do ZAPI
        response = requests.post(url, json=payload)

        # Verificar a resposta da API
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            
        
        
        return response.status_code, response.text
        
    except requests.RequestException as e:
        print("Erro de conexão com a API do ZAPI:", str(e))
        return None, str(e)



def enviar_mensagens_em_massa():
    contatos = get_supabase_client()
    for contato in contatos:
        enviar_mensagem(contato['nome'], contato['telefone'])
        
    