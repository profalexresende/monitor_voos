import os
import requests

# Suas listas de aeroportos
origens = ["GRU", "VCP", "CGH"]
destinos = ["REC", "SSA","NAT"] 

# Configurações fixas
PRECO_TETO = 2500
API_KEY = os.getenv("SERPAPI_KEY")

# Loop para testar todas as combinações (GRU -> REC, GRU -> SSA, VCP -> REC...)
for origem in origens:
    for destino in destinos:
        print(f"\n🔍 Pesquisando voos de {origem} para {destino}...")

        params = {
            "engine": "google_flights",
            "departure_id": origem,
            "arrival_id": destino,
            "outbound_date": "2026-10-15",
            "return_date": "2026-10-22",
            "currency": "BRL",
            "hl": "pt-br",
            "gl": "br",
            "api_key": API_KEY,
        }

        response = requests.get("https://serpapi.com/search", params=params)
        dados = response.json()

        # Verifica se retornou voos válidos
        if "best_flights" in dados:
            menor_preco = dados["best_flights"][0]["price"]
            print(f"[{origem} -> {destino}] Menor preço: R$ {menor_preco}")

            if menor_preco <= PRECO_TETO:
                print(f"🎉 PROMOÇÃO! {origem} -> {destino} por R$ {menor_preco}")
        else:
            print(f"Nenhum voo encontrado para {origem} -> {destino}.")
