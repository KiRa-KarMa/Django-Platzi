
# Consola interactiva de Django

Para activar la shell de Django:
```sh
python manage.py shell
```

Dentro de la shell:
```sh
from polls.models import Question, Choice

# Para obtener todos los registros de preguntas de la base de datos
Question.objects.all()

# Modulo para añadir zopnas horarias
from django.utils import timezone

# Creamos una pregunta de esta forma y la almacenamos en la variable q
q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=timezone.now()) 

# Para guardarlo
q.save()
```

Despues de crear la question, al poner `Question.objects.all()` nos devolverá `<Question: Question object (1)>`, para que nos devuelva algo más agradable
al llamarlo vamos a crear dos metodos nuevos en la clase de Question del modelo.

Nos quedaría así:
```sh
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Ahora  `Question.objects.all()` nos devolverá `<QuerySet [<Question: ¿Cual es el mejor curso de Platzi?>]>`



