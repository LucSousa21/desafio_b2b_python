import os
from supabase import create_client

# Função para obter dados do Supabase
def get_supabase_client():

    try:
        # Carregar variáveis de ambiente    
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_ANON_KEY")

        # Criar cliente do Supabase
        supabase = create_client(url, key)
        # Realizar consulta para obter contatos
        response = supabase.table("contatos").select("*").limit(3).execute()

        return response.data
    
    except Exception as e:
        print("Erro ao conectar ao Supabase:", str(e))
        return []
