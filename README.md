# Challenge
# Instrucciones:
# Antes de poder interactuar con los componentes dela página web, tiene que crearse un usuario.
# Posteriormente si usted desde la consola no ha sido colocado como administrados, no podrá crear retos nuevos en el sistema.
# Puede asignar una foto del reto cumplido al dar clic en Cumple tu reto.
# Dentro de Apartado artístico podrá colocar los poemas y dibujos creados.
# Ranking es una imagen meramente ilustrativa, pero se mostrará como una tabla con los usuarios con el mejor puntaje.
# Puntos obtenidos es también ilustrativo, solo será para visualización de puntos recolectados por el usuario. 

## Instalación del ambiente

### Requerimientos

- Python con las versiones mas recientes

### Ubuntu Linux 
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Activación de la ejecución de scrips para PowerShell (Ejecutar PowerShell como administrados)
~~~
Set-ExecutionPolicy Unrestricted
~~~
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles Iniciar servidor
#### Linux 
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~
