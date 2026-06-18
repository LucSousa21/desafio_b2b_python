from dotenv import load_dotenv
from zapi_mensagem import enviar_mensagens_em_massa
load_dotenv()  # Carregar variáveis de ambiente do arquivo .env
if __name__ == "__main__":
    
    enviar_mensagens_em_massa()
