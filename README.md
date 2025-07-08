
# Project Title

A brief description of what this project does and who it's for

# Proyecto-Dos

Este proyecto consiste en una API RESTful simple desarrollada con Flask para gestionar plantas, videojuegos y generos de videojuegos

## Tecnología Utilizadas
* **Python 3.13.5**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLite**
* **Docker**
* **Docker Compose**

## Cómo empezar

Seguir los siguiente pasos para poner en marcha la aplicacion:

1. **Clona el repositorio:**
```bash
git clone https://github.com/Jigoro-Miyamoto/Proyecto-Dos
cd Proyecto-Dos
```
2. **Configura las variables de entorno:**

Crea un archivo '.env' en la raiz de tu protecto en donde definiras el puerto que usaras:
```bash
PORT = 5000
```
Puedes usar cualquier puerto que tengas disponible 

3. **Inicializar Aplicación**:

Puedes iniciar la aplicación de dos maneras:
* Docker Compose
* Python
#### A) Usando Docker Compose
Asegurate de tener Docker Desktop instalado y en ejecución, luego en tu terminal ejecuta:
```bash
docker-compose up --build
```
* Esto construirá la imagen y levantará tu API. La primera vez, puede tardar un poco.
* La aplicación será accesible a través del puerto definido en tu archivo .env
#### B) Usando Python localmente

1. **Configura un entorno virtual** (recomendado):
```bash
pip install -r requirements.txt
```
2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configura las variables de entorno para Flask y el Puerto:**
    * **En Linux/macOS:**
        ```bash
        export FLASK_APP=app.py
        export FLASK_ENV=development
        export PORT=5000 # O el puerto que desees, ej. 8000
        ```
    * **En Windows (CMD):**
        ```cmd
        set FLASK_APP=app.py
        set FLASK_ENV=development
        set PORT=5000 # O el puerto que desees, ej. 8000
        ```
    * **En Windows (PowerShell):**
        ```powershell
        $env:FLASK_APP="app.py"
        $env:FLASK_ENV="development"
        $env:PORT="5000" # O el puerto que desees, ej. 8000
        ```
    *(Nota: Si no defines `PORT`, la aplicación por defecto usará el puerto 5000 como configurado en `app.py`.)*
4.  **Ejecuta la aplicación:**
    ```bash
    python app.py
    ```
5.  La API estará disponible en `http://localhost:[TU_PUERTO]`.

## Endpoints de la API

* **VideoJuegos ('/juegos)** 
    * 'GET /juegos': Obtener todos los videojuegos.
    * 'GET /juegos/<id>': Obtener videojuego por su ID.
    * 'POST /juegos': Crear un nuevo videojuego.
    * 'PATCH /juegos/<id>': Actualizar un videojuego.
    * 'DELETE /juegos/<id>': Eliminar un videojuego.
* **Plantas ('/plantas)** 
    * 'GET /plantas': Obtener todas las plantas.
    * 'GET /plantas/<id>': Obtener planta por su ID.
    * 'POST /plantas': Crear una nueva planta.
    * 'PATCH /plantas/<id>': Actualizar una planta.
    * 'DELETE /plantas/<id>': Eliminar una planta.
* **VideoJuegos ('/juegos)** 
    * 'GET /generos': Obtener todos los géneros.
    * 'GET /generos/<id>': Obtener género por su ID.
    * 'POST /generos': Crear un nuevo género.
    * 'PATCH /generos/<id>': Actualizar un género.
    * 'DELETE /generos/<id>': Eliminar un género.
    
## Colecciones de Postman

Puedes encontrar las colecciones de Postman en la carpeta 'postman/' de este repositorio.

## Notas
- La base de datos utilizada por defecto es **SQLite**, por lo que no es necesaria alguna configuracion adicional para correr localmente

- Recuerda mapear correctamente el puerto configurado si usas Docker

## Contribuciones
Si encuentras errores o quieres mejorar alguna funcionalidad, no dudes en abrir un **issue** o enviar un **pull request**.
    