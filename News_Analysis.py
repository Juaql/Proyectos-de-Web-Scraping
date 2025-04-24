import requests
from bs4 import BeautifulSoup
import csv

# Funcion para obtener links
def obtener_links_de_noticias(url, response, themes, links):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar todos los enlaces que podrían ser noticias
        enlaces = soup.find_all('a', href=True)

        for enlace in enlaces:
            href = enlace['href']
            link_completo = href if href.startswith("http") else url + href.lstrip('/')

            if any(t in href for t in themes):
                links.add(link_completo)
    else:
        print(f"Error al acceder a la página: {response.status_code}")


# Borramos archivo antes de comenzar para evitar duplicados si ejecutás varias veces
with open('links_noticias.csv', mode='w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerow(["Enlace"])

# Variables
thu_url = "https://www.thedailyupside.com/"
thu_themes = ["economics", "finance", "technology",
              "business", "industries", "investments",
              "newsletters"]
links = set()

# Iteramos por tema
for tema in thu_themes:
    full_url = thu_url + tema + '/'
    response = requests.get(full_url)
    obtener_links_de_noticias(thu_url, response, thu_themes, links)

with open('links_noticias.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(["Enlace"])
    for link in links:
        escritor.writerow([link])

# Leectura del articulo
def leer_articulo():
    with open('links_noticias.csv', mode='r', encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for i, fila in enumerate(lector, 1):
            url = fila[0]
            try:
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    parrafos = soup.find_all(['p', 'h2', 'ul'])

                    for p in parrafos:
                        texto = p.get_text(strip=True)
                        if texto:
                            print(texto)
                else:
                    print(f"Error {response.status_code}")
            except Exception as e:
                print(f"Excepción al procesar la URL: {e}")

leer_articulo()
