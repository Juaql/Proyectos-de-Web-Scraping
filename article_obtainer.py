import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
from urllib.parse import urlparse

# Confirmar que probablemente sea un articulo
def es_url_articulo(url):
    """
    Determina si una URL probablemente corresponde a un artículo.
    Se considera que una URL es de un artículo si tiene al menos tres segmentos en su ruta.
    """
    path = urlparse(url).path
    segmentos = path.strip('/').split('/')
    return len(segmentos) >= 3

# Funcion para obtener links
def obtener_links_de_noticias(url, response, themes, links):
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        enlaces = soup.find_all('a', href=True)

        for enlace in enlaces:
            href = enlace['href']
            # Construir la URL completa
            link_completo = href if href.startswith('http') else url.rstrip('/') + '/' + href.lstrip('/')

            # Verificar si el enlace contiene alguno de los temas y si es una URL de artículo
            if any(t in href for t in themes) and es_url_articulo(link_completo):
                links.add(link_completo)
    else:
        print(f"Error al acceder a la página: {response.status_code}")


# Borramos archivo antes de comenzar para evitar duplicados si ejecutás varias veces
with open('links_noticias.csv', mode='w', newline='', encoding='utf-8') as f:
    csv.writer(f)

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
    for link in links:
        escritor.writerow([link])

# Crear base de datos SQL
def crear_base_de_datos(nombre_db='noticias.db'):
    conn = sqlite3.connect(nombre_db)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            contenido TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Almacenar datos
def guardar_articulo_en_db(url, contenido, nombre_db='noticias.db'):
    conn = sqlite3.connect(nombre_db)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO articulos (url, contenido) VALUES (?, ?)
    ''', (url, contenido))

    conn.commit()
    conn.close()

# Leectura del articulo
def leer_y_guardar_articulos():
    with open('links_noticias.csv', mode='r', encoding='utf-8') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for i, fila in enumerate(lector, 1):
            url = fila[0]
            try:
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    parrafos = soup.find_all(['p', 'h2', 'ul'])

                    texto = "\n".join([p.get_text(strip=True) for p in parrafos if p.get_text(strip=True)])
                    print(texto)
                    if texto:
                        guardar_articulo_en_db(url, texto)
                        print(f"[{i}] Guardado correctamente: {url}")
                    else:
                        print(f"[{i}] Artículo sin contenido: {url}")
                else:
                    print(f"[{i}] Error {response.status_code} en: {url}")
            except Exception as e:
                print(f"[{i}] Excepción con {url}: {e}")

crear_base_de_datos()
leer_y_guardar_articulos()