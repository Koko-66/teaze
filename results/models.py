""""Test """
from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz
from questions.models import Option, Question


class Assessment(models.Model):
    """Crate assessment"""

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='assessment')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz}-{self.user}'

    # def get_answers(self):
    #     return self.answer_set.all()


class Answer(models.Model):
    """Create user answer"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answered_question')
    answer = models.IntegerField()
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE,
                                   related_name='answer')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.question)} - {self.answer}'
