from django.test import TestCase
from django.utils import timezone
import datetime
from polls.models import Question

# Testeamos o Modelos o Vistas
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor Course Director de Platzi?", pub_date=time)
        # Afirma si la ejecución de esa función devuelve False
        self.assertIs(future_question.was_published_recently(), False)