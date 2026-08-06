import os
import requests

# Puxa a chave dos Segredos (Secrets) do GitHub Actions ou usa um valor padrão
API_KEY = os.getenv("SERPAPI_KEY", "SUA_API_KEY_AQUI")

# Configurações da Busca
ORIGEM = "GRU"
DESTINO = "REC"
DATA_IDA = "2026-12-31"
DATA_VOLTA = "2027-01-08"
PRECO_MAXIMO = 10000

def buscar_voos():
    url = "https://serpapi.com/search"
    
    params = {
        "engine": "google_flights",
        "departure_id": ORIGEM,
        "arrival_id": DESTINO,
        "outbound_date": DATA_IDA,
        "return_date": DATA_VOLTA,
        "currency": "BRL",
        "hl": "pt-br",
        "gl": "br",
        "api_key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        dados = response.json()
        
        if "best_flights" in dados:
            voos = dados["best_flights"]
            melhor_preco = voos[0]["price"]
            
            print(f"[{ORIGEM} -> {DESTINO}] Menor preço encontrado: R$ {melhor_preco}")
            
            if melhor_preco <= PRECO_MAXIMO:
                enviar_alerta(melhor_preco, voos[0])
            else:
                print("Preço ainda está acima do teto desejado.")
        else:
            print("Nenhum voo encontrado ou erro na resposta da API.")
            print("Resposta da API:", dados)
            
    except Exception as e:
        print(f"Erro ao consultar a API: {e}")

def enviar_alerta(preco, detalhes):
    print("\n" + "!"*40)
    print(f"🎉 PROMOÇÃO ENCONTRADA! Voo por R$ {preco}")
    print("!"*40 + "\n")

if __name__ == "__main__":
    buscar_voos()
