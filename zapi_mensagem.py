import os, requests
from urllib import response
from conect_supabase import get_supabase_client

def enviar_mensagem(nome, telefone):
    url = os.getenv("ZAPI_INSTANCE_URL")
    token = os.getenv("ZAPI_TOKEN")

    payload = {
        "phone": telefone,
        "message": f"Olá {nome}, tudo bem?"
    }

    response = requests.post(url, json=payload, headers={"Authorization": f"Bearer {token}"})
    print(response.status_code)
    print(response.text)
    if response.status_code != 200:
        print("Error: ", response.status_code)

if __name__ == "__main__":
    dado = get_supabase_client()
    enviar_mensagem(dado[1]['nome'], dado[1]['telefone'])
    