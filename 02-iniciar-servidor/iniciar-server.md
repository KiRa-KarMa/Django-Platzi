

# Iniciar servidor en Django

En la carpeta del proyecto, ejecutamos el siguiente comando y nos abrirá un servidor de
Django en el puerto 8000 (Puerto predeterminado)
```sh
python manage.py runserver
```

Para inciar con otro puerto
```sh
python manage.py runserver 9999
```


# ORGANIZACIÓN DE DJANGO

Django se organiza en 'Proyectos' y 'Aplicaciones'. Los Proyectos son un conjunto de Aplicaciones.

Por ejemplo el proyecto INSTAGRAM tiene varias apps:

    - Feed
    - Stories
    - Chats
    ...

Para nuestro proyecto de PremiosPlatziApp

    - Polls