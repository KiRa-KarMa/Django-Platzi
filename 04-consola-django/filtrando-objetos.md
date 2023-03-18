
# GET

Para filtrar un objeto usamos get. El metodo get trae solo un objeto, si devuelve mas de un objeto la consulta falla.

El parametro pk=primary_key

```sh
Question.objects.get(pk=1)
```


# FILTER

Para filtrar varios objetos. Devuelve un conjunto vacío si no encuentra ningun objeto que coincida con las condiciones.
```sh
Question.objects.filter(pk=1)

# Para traer todas las preguntas que sean de este año
# Con los atributos de django se puede usar __ para más características del atributo por ejemplo pub_date__year
Question.objects.filter(pub_date__year=timezone.now().year)

# Otro ejemplo question_text__startswith
Question.objects.filter(question_text__startswith="¿Cual")
```

# CREATE

Cuando tenemos una relación 1 a N, tenemos la opcion choice_set para obtener la filas. En este caso para obtener las respuestas (N) de una pregunta (1) 

```sh
q = Question.objects.get(pk=1)    
q.choice_set.all()
```

Para crear una respuesta, podemos hacer de la misma forma que la pregunta, Choice(choice_text="Curso de Fun....
Pero nos encontramos con el problema de las claves entre otros.
Para solucionarlo lo mejor es crear las respuestas a partir de la pregunta.

```sh
q = Question.objects.get(pk=1)    
q.choice_set.create(choice_text="Curso de Wordpress", votes=0) 
q.choice_set.create(choice_text="Curso Fundamentos de Ingenieria de Software", votes=0)
```

Para obtener el numero de respuestas:

```sh
q.choice_set.count()
```

Para filtrar las respuestas que sean de este año:
```sh

# question__pub_date__year -> question__pub_date = pub_date de la question a la que pertenece la pregunta
Choice.objects.filter(question__pub_date__year=timezone.now().year) 
```

[Ejemplo de queries de Django](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro)