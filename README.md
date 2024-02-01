# Dessert

Proyecto escolar que trata de un sitio web de postrería usando Django.

## Requisitos Previos

Asegúrate de tener instalado Python en tu máquina. Puedes descargarlo desde [python.org](https://www.python.org/).

## Configuración del Entorno Virtual

```bash
# Crear un entorno virtual
python -m venv myenv

# Activar el entorno virtual
myenv\Scripts\activate   # Windows
source myenv/bin/activate # Linux/Mac

# Instalar las dependencias del proyecto
pip install -r requirements.txt

# Aplicar migraciones a la base de datos
python manage.py migrate

# Iniciar el servidor de desarrollo
python manage.py runserver
```

Abre tu navegador y accede a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.