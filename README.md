# Clonar y ejecutar el programa

Para clonar y ejecutar este programa, sigue los siguientes pasos:

# Prerrequisitos

Asegúrate de tener instalados los siguientes componentes en tu sistema:
- **Python**: Puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).
- **pip**: Normalmente se instala junto con Python, pero si no lo tienes, puedes seguir las instrucciones en [pip.pypa.io](https://pip.pypa.io/en/stable/installation/).


1. **Clonar el repositorio**  
    Abre tu terminal y ejecuta el siguiente comando:
    ```bash
    git clone https://github.com/Soinekro/procesar_urls.git
    ```

2. **Navegar al directorio del proyecto**  
    ```bash
    cd procesar_urls 
    ``` 

5. **Instalar las dependencias**  
    ```bash
    pip install -r requirements.txt
    ```

6. **Ejecutar el programa**  
    ```bash
    python procesar.py
    ```


# Uso de `python` en proyectos de [ciencia de datos](https://www.ibm.com/es-es/topics/data-science)
lleve un curso de [ciencia de datos](https://pit-virtual.uni.edu.pe/pluginfile.php/71561/mod_resource/content/1/Separata01.pdf) de la Universidad Nacional de Ingeniería de Lima y un pequeño [curso](https://github.com/Soinekro/alura-datos1) de [alura latan](https://www.aluracursos.com/), que esta en [mi github](https://github.com/Soinekro) donde nos enseñaron a usar python con la libreria [pandas](https://pandas.pydata.org/) y [matplotlib](https://matplotlib.org/) de lo cual aprendi la facilidad del procesamiento de datos en memoria que tiene con grandes volumenes de datos.

## ¿Qué es `pandas`?

`pandas` es una biblioteca de Python que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar. Es ampliamente utilizada en el análisis de datos, especialmente en el contexto de ciencia de datos.

## ¿Por qué se usa en ciencia de datos?

`pandas` se utiliza en ciencia de datos por varias razones:

1. **Manejo de grandes archivos**: `pandas` puede leer y escribir grandes archivos de datos en varios formatos (CSV, Excel, SQL,txt, etc.).
2. **Procesamiento eficiente**: Ofrece operaciones rápidas y eficientes para manipular y analizar datos.
3. **Flexibilidad**: Permite realizar operaciones complejas de datos con facilidad, como filtrado, agrupamiento y agregación.

Estas estructuras permiten realizar operaciones de datos de manera eficiente y con un uso óptimo de la memoria.

## Técnicas de optimización de rendimiento y uso de memoria

1. **Uso de tipos de datos adecuados**: Convertir columnas a tipos de datos más eficientes (por ejemplo, `int` en lugar de `float`).
2. **Lectura por partes**: Leer grandes archivos en partes más pequeñas para evitar el uso excesivo de memoria.
3. **Operaciones vectorizadas**: Utilizar operaciones vectorizadas en lugar de bucles para mejorar la velocidad de procesamiento.
4. **Uso de `chunksize`**: Procesar datos en fragmentos (`chunks`) para manejar archivos grandes sin cargar todo en la memoria.

Estas técnicas ayudan a `pandas` a manejar grandes volúmenes de datos de manera eficiente y efectiva.
