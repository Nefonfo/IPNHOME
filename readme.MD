# **IPN HOME - DJANGO**

## Requisitos
- python 3.8.X
- pip 21.2.X
- virtualenv (se explicara como instalarlo)

## Instrucciones para correr el programa (considerando que ya tienes python y pip)

1. Primero instalaremos el virtualenv
```console
C:\Users\vicmi> pip install virtualenv
C:\Users\vicmi> virtual --version
```
Si te muestra la versión de virtualenv, ya quedo

2. Despues clona el repositorio
```console
C:\Users\vicmi> git clone <inserta url de la repo>
```

3. Accede a la raiz del proyecto

4. Ejecuta el comando para crear nuestro entorno virtual de python

```console
C:\Users\vicmi\ipnhome> virtualenv env
```

5. Activaremos nuestro entorno virtual de python

```console
C:\Users\vicmi\ipnhome> cd ./env/Scripts
C:\Users\vicmi\ipnhome\env> activate && cd ../../
(env) C:\Users\vicmi\ipnhome>
```
si te sale el "(env)" significa que ya tienes activado el entorno virtual

* Si deseas salir de el entorno realiza el siguiente comando
```console
(env) C:\Users\vicmi\ipnhome> cd ./env/Scripts
(env) C:\Users\vicmi\ipnhome\env> deactivate && cd ../../
C:\Users\vicmi\ipnhome>
```

6. Regresamos a la carpeta raíz

7. Instalaremos los paquetes necesarios del proyecto (en nuestro entorno virtual para no ensuciar el python instalado)

```console
C:\Users\vicmi\ipnhome> pip install -r requirements.txt
```

8. Generaremos la base de datos con el siguiente comando

```console
(env) C:\Users\vicmi\ipnhome> python manage.py migrate
```

9. Generaremos la semilla de nuestras Unidades académicas **(este paso es opcional pero altamente recomendable)**

```console
(env) C:\Users\vicmi\ipnhome> python manage.py runscript academic_unit_seed
```

10. Generaremos nuestro usuario administrador con el siguiente comando (este nos dará instrucciones de que introducir)

```console
(env) C:\Users\vicmi\ipnhome> python manage.py createsuperuser
```

11. Iniciaremos el servidor de Django
```console
(env) C:\Users\vicmi\ipnhome> python manage.py runserver
```

12. Las siguientes rutas son las adecuadas para ingresar

    * **localhost:8000** -> página de inicio no modificada
    * **localhost:8000/admin** -> administrador
    * **localhost:8000/accounts/login** -> inicio de sesión de usuarios normales y también administrador


## Consideraciones opcionales

Para agregar alumnos de manera rápida, viene de manera opcional dentro del proyecto (ruta: ./student/example.json) un json con la estructura que lleva la importación masiva de alumnos, **considera que al crear un alumno generará su usuario, en caso de uno proporcionar su email generara uno a partir de su boleta (boleta@ipn.mx) y siempre la contraseña será su boleta (inicialmente)**, en caso de tener mal tu estructura json, te avisará el error y ningún usuario del json será creado