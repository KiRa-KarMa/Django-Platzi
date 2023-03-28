from django.test import TestCase
from django.utils import timezone
import datetime
from polls.models import Question
from django.urls.base import reverse
import datetime

# Testeamos o Modelos o Vistas
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        # Afirma si la ejecución de esa función devuelve False
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days=0):
    """
    Create a question with the given "question_text", and published the givem numbrer of days offset to now
    (negative for questions published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question(question_text=question_text, pub_date=time).save()


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exist, an apropiate message is displayed"""

        # Realizamos una petición http a nuestra url de index.
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    
    def test_future_questions(self):
        """No future questions must be visible"""
        create_question('Future Question', 50)

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_past_questions(self):
        """past questions are displayed"""
        create_question('Past Question', -50)

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No polls are available.")