from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Answer, Assessment
from quiz.models import Quiz
from questions.models import Question, Option


class TakeQuizView(ListView):
    """Quiz completion view per page"""
    # model = Quiz

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

        user = request.user
        score = 0
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.get_questions()

        if request.method == "POST":
            assessment = Assessment.objects.create(user=user, quiz=quiz,
                                                score=score)
            raw_data = dict(request.POST.items())  # gets dict:question_id:option_id
            answered_questions = list(raw_data.keys())
            answers = list(raw_data.values())
            del answers[0]
            del answered_questions[0]

            data = []
            for q, a in zip(answered_questions, answers):
                answered_question = Question.objects.get(id=int(q))
                if a != '0':
                    response = Option.objects.get(id=int(a))
                    if response.is_correct:
                        score += 1
                else:
                    response = None
                print(score)

                data.append((answered_question, response))
                answer = Answer.objects.create(question=answered_question, answer=response,
                                            assessment=assessment)

            assessment.score = score
            context = {
                        'answer': answer,
                        'assessment': assessment,
                        'questions': questions,
                    }
            print(data)
            return render(request, 'results/results.html', context)

        return reverse('results/results.html') 


class AssessmentView(DetailView):
    model = Assessment
    template_name = 'results/results.html'


# def save_results(request, slug):
#     """Get and process answers to the quiz and return feedback"""
#     user = request.user
#     score = 0
#     quiz = get_object_or_404(Quiz, slug=slug)
#     questions = quiz.get_questions()
    
#     number_of_questions = len(questions)

#     if request.method == "POST":
#         assessment = Assessment.objects.create(user=user, quiz=quiz,
#                                                score=score)
#         raw_data = dict(request.POST.items())  # gets dict:question_id:option_id
#         answered_questions = list(raw_data.keys())
#         answers = list(raw_data.values())
#         del answers[0]
#         del answered_questions[0]

#         data = []
#         for q, a in zip(answered_questions, answers):
#             answered_question = Question.objects.get(id=int(q))
#             if a != '0':
#                 response = Option.objects.get(id=int(a))
#                 # data.append((answered_question, response))
#                 if response.is_correct:
#                     score += 1
#             else:
#                 response = None
#             print(score)

#             data.append((answered_question, response))
#             answer = Answer.objects.create(question=answered_question, answer=response,
#                                            assessment=assessment)
#         assessment.score = score
#         template_name = "results/results.html"
#         context = {
#                     'answer': answer,
#                     'assessment': assessment,

#                     'questions': questions,
#                     'number_of_questions': number_of_questions,
#             }
#         print(data)
#         return render(request, template_name, context)