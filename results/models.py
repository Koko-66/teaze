""""Assessment and answer models"""
from django.db import models
from django.contrib.auth.models import User
from questions.models import Option, Question
from quiz.models import Quiz


class Assessment(models.Model):
    """Crate an instance of assessment"""

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='assessment')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.user} - {self.quiz}'

    def get_answers(self):
        return self.answer.all()


class Answer(models.Model):
    """Create an instance of ansawer"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answered_question')
    answer = models.ForeignKey(Option, on_delete=models.PROTECT,
                               null=True, related_name='answer_option')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE,
                                   related_name='answer')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.question)} - {self.answer}'
