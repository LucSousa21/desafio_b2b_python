import os
from dotenv import load_dotenv
from supabase import create_client

def get_supabase_client():
        
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_ANON_KEY")


    supabase = create_client(url, key)

    response = supabase.table("contatos").select("*").limit(3).execute()

    
    return response.data