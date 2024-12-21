import os
import tarfile
import urllib
import urllib.request 
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_and_prepare_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Descarga y descomprime el archivo housing.tgz en la ruta especificada.
    """
    print(f"Creando directorio en {housing_path} si no existe...")
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    
    print(f"Descargando datos desde {housing_url}...")
    urllib.request.urlretrieve(housing_url, tgz_path)
    print(f"Datos descargados en: {tgz_path}")
    
    print("Extrayendo datos...")
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)
    print(f"Datos extraídos en: {housing_path}")

# Ejecuta la función cuando se llama directamente
if __name__ == "__main__":
    fetch_and_prepare_data()
