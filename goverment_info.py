import requests
import zipfile

# URL del archivo DB (verde cemento)
url = "https://apis.datos.gob.ar/series/api/dump/sspm/series-tiempo-sqlite.zip"
nombre_archivo = "series-tiempo-sqlite.zip"

try:
    respuesta = requests.get(url, timeout=30)
    respuesta.raise_for_status()

    with open(nombre_archivo, "wb") as archivo:
        archivo.write(respuesta.content)

    print(f"Archivo descargado correctamente: {nombre_archivo}")
except requests.exceptions.RequestException as e:
    print(f"Error al descargar el archivo: {e}")

with zipfile.ZipFile(nombre_archivo, 'r') as zip_ref:
    zip_ref.extractall("datos_sqlite")
    print("Archivo descomprimido en la carpeta 'datos_sqlite'")
