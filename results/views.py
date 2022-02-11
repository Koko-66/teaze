from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Answer, Assessment
from quiz.models import Quiz
from questions.models import Question, Option


class TakeQuizView(ListView):
    """Quiz completion view (in one page)."""

    def get(self, request, slug):
        """Overwrite the built-in get method to get the questions queryset"""

        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.get_questions()
        context = {
            'questions': questions,
            'quiz': quiz,
        }
        return render(request, 'results/take_quiz.html', context)

    def post(self, request, slug):
        """Overwrite the built-in post method."""

        user = request.user
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.get_questions()

        if request.method == "POST":
            # get dict:question_id:option_id
            raw_data = dict(request.POST.items())
            answered_questions = list(raw_data.keys())
            answers = list(raw_data.values())
            del answers[0]
            del answered_questions[0]

            # data = []
            score = 0
            # create blank assessment
            assessment = Assessment.objects.create(user=user, quiz=quiz,
                                                   score=score)
            for q, a in zip(answered_questions, answers):
                answered_question = Question.objects.get(id=int(q))
                if a != '0':
                    response = Option.objects.get(id=int(a))
                    if response.is_correct:
                        score += 1
                else:
                    response = None
                    print(score)
                # data.append((answered_question, response))
                answer = Answer.objects.create(question=answered_question,
                                               answer=response,
                                               assessment=assessment)

            # update assessment with the updated score for the quiz
            Assessment.objects.update(score=score)
            context = {
                        'answer': answer,
                        'assessment': assessment,
                        'questions': questions,
                    }
            # print(data)
            assessment.score = score
            return render(request, 'results/results.html', context)
        # return reverse('results/results.html')


class AssessmentView(DetailView):
    model = Assessment
    template_name = 'results/results.html'
