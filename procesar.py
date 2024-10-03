import re
import pandas as pd

def procesar_urls(archivo_entrada):
    urls_unicas = set()  # Utilizamos un conjunto para eliminar duplicados automáticamente
    patron_dominio = re.compile(r'https?://(.*?shop.*?)/.*\.html$')  # Patrón para filtrar URLs que contienen 'shop' y terminan con '.html'

    try:
        # Leer el archivo en fragmentos (chunks) para evitar cargar todo el archivo en memoria
        chunk_size = 1000  # Leer 1,000 líneas a la vez
        for chunk in pd.read_csv(archivo_entrada, header=None, names=['url'], encoding='utf-8', chunksize=chunk_size):
            # Aplicar el filtro utilizando una operación vectorizada
            urls_filtradas = chunk['url'].str.strip().str.contains(patron_dominio)
            urls_unicas.update(chunk[urls_filtradas]['url'].tolist()) # Agregar las URLs únicas al conjunto

        # Imprimir las URLs que cumplen con los criterios
        for url in urls_unicas:
            print(url)

        # Mostrar el total de URLs que cumplen con los criterios
        print(f"\nTotal de URLs que cumplen con los criterios: {len(urls_unicas)}")

    except FileNotFoundError:  # Si el archivo no se encuentra en el directorio
        print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'.")

# Ejecutar el programa
if __name__ == "__main__":  # Si el script se ejecuta directamente
    archivo_entrada = 'urls.txt'  # Nombre del archivo de texto con las URLs
    procesar_urls(archivo_entrada)
