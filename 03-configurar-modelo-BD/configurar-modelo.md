

# Configurar modelo de base de datos

Vamos a /polls/models.py y escribimos el modelo de datos de nuestras tablas:

```sh
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")



class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```


Ahora vamos a settings.py de nuestro proyecto y en INSTALLED_APPS añadimos a la lista:

Es el archivo apps.py y la clase PollsConfig

```sh
"polls.apps.PollsConfig",
```

Tras esto en la terminal escribimos estos comandos para realizar la migración:

Crea un archivo en /polls/migrations llamado 0001_initial.py en el que Django automaticamente
describe toda creación de las tablas en la base de datos usando ORM.
```sh
python .\manage.py makemigrations polls
```

Toma el archivo que se creo y lo usa usando SQL en la base de datos.
```sh
python .\manage.py migrate
```