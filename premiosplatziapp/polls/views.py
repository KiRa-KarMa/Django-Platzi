from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone


# Class Based Views
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        # Se pone -pub_date para traer de recientes a antiguas, sin el guión lo haría al revés
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    # Esto es lo que se va a guardar en la variable que hemos llamado latest_question_list y que hemos
    # configurado en context_object_name


class DetailView(generic.DetailView):
    model = Question # Esto sustituye a get_object_or_404(Question, pk=question_id)
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question # Esto sustituye a get_object_or_404(Question, pk=question_id)
    template_name = "polls/results.html"



# Function Views
# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })


# def detail(request, question_id):
#     # get_object_or_404 Sirve para traernos las preguntas o devolver un error 404
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {
#         "question": question
#     })


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })


def vote(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Es una buena practica redirigir al usuario usando HttpResponseRedirect
        # reverse sirve al igual que html pero en python para no hardcodear una url
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))