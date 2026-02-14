import pandas as pd
import requests
import sqlite3
from datetime import datetime

def executar_pipeline():
    print("--- Iniciando o Pipeline ---")
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            print("1. Dados reais coletados com sucesso.")
        else:
            print(f"Aviso: Limite de API atingido (Erro {response.status_code}). Usando dados de teste...")
            dados = {
                'USDBRL': {'code': 'USD', 'bid': '5.00'},
                'EURBRL': {'code': 'EUR', 'bid': '5.40'}
            }
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return

    # Transformação e Carga
    try:
        lista_moedas = []
        for chave in dados:
            item = dados[chave]
            lista_moedas.append({
                'moeda': item['code'],
                'valor': float(item['bid']),
                'data_consulta': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        df = pd.DataFrame(lista_moedas)
        conn = sqlite3.connect('cotacoes.db')
        df.to_sql('precos', conn, if_exists='append', index=False)
        conn.close()
        print("2. SUCESSO: O arquivo 'cotacoes.db' foi criado/atualizado!")
    except Exception as e:
        print(f"Erro no processamento: {e}")

if __name__ == "__main__":
    executar_pipeline()
