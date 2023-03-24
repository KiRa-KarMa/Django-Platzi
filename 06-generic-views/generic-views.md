

Tenemos las Function Views (que usan funciones) y las Class Based Views (que usan clases).

Para no repetir codigo (DRY -> Don't Repeat Yourself) Django tiene las llamadas Generic Views o Class Based Views.

Tenemos por ejemplo:

ListView -> Viendo los tweets
LoginView -> Login en Twitter
LogoutView -> Saliendo de Twitter
CreateView -> Creando Tweet
UpdateView -> Modificar el perfil de Twitter
DeleteView -> Borrando un tweet


## Cuanto usar Generic Views y cuando Function Views???

Generic Views:
Si se usa un patrón de
    - Cargar datos de la BD
    - Genero un Template
    - Muestro Template

Function Views:
    Si nos escapamos del patrón de Generic Views.