

# ADMINISTRADOR DE DATOS DE DJANGO

Empezaremos creando un usuario de administrador usando el comando:
```sh
python manage.py createsuperuser
```

Despues de crear el usuario vamos al archivo admin.py de nuestra app en polls/admin.py
y añadimos las siguientes lineas:

```sh
# Importamos nuestros modelos
from .models import Question, Choice

# Registramos en el admin los modelos
admin.site.register([Question, Choice])
```