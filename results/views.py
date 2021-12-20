from django.shortcuts import render, get_object_or_404
# from django.views import generic, View
from .models import Answer, Assessment
from quiz.models import Quiz
# from quiz.views import QuizDetailsView
from questions.models import Question, Option


def results(request, slug):
    user = request.user
    score = 0
    completed = False
    quiz = get_object_or_404(Quiz, slug=slug)
    questions = []
    for question in quiz.get_questions():
        options = []
        for option in question.get_options():
            options.append(option)
        questions.append({question: options})
    number_of_questions = len(questions)

    if request.method == "POST":
        raw_data = dict(request.POST.items())  # gets dict:question_id:option_id
        answered_questions = list(raw_data.keys())
        answers = list(raw_data.values())
        del answers[0]
        del answered_questions[0]

        data = []
        for q, a in zip(answered_questions, answers):
            answered_question = Question.objects.get(id=int(q))
            answer = Option.objects.get(id=int(a))
            data.append((answered_question, answer))
            if answer.is_correct:
                score += 1
        assessment = Assessment.objects.create(user=user, quiz=quiz,
                                               score=score)
        template_name = "results/results.html"
        context = {
                    'data': data,
                    'answered_question': answered_question,
                    'answer': answer,
                    'assessment': assessment,
                    'quiz': quiz,
                    'questions': questions,
                    'number_of_questions': number_of_questions,
                    # 'completed': completed,
            }

        return render(request, template_name, context)
