import requests
from bs4 import BeautifulSoup

def buscar_alquimia(termo):
    url = "https://en.uesp.net/wiki/Skyrim:Useful_Potions"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        tabelas = soup.find_all('table')
        resultados = []
        termo_low = termo.lower()

        for tabela in tabelas:
            for linha in tabela.find_all('tr'):
                texto_linha = linha.get_text(" ", strip=True).lower()
                
                if termo_low in texto_linha:
                    colunas = linha.find_all(['td', 'th'])
                    
                    if len(colunas) >= 2:
                        efeito = colunas[0].get_text(" ", strip=True)
                        ingredientes = colunas[1].get_text(" ", strip=True)
                        
                        if "effect" in efeito.lower() and "ingredients" in ingredientes.lower():
                            continue
                            
                        resultados.append({
                            "Efeito": efeito,
                            "Ingredientes": ingredientes
                        })
        
        return resultados

    except Exception as e:
        return []

if __name__ == "__main__":
    print("--- Alchemist Scraper SSE ---")
    busca = input("Qual poção ou efeito você deseja consultar? ").strip()

    if busca:
        lista = buscar_alquimia(busca)

        if lista:
            print(f"\n Achei {len(lista)} resultado(s):")
            print("=" * 60)
            for item in lista:
                print(f" {item['Efeito']}")
                print(f" {item['Ingredientes']}")
                print("-" * 60)
        else:
            print(f" '{busca}' não encontrado. Tente apenas 'Block' ou 'Health'.")