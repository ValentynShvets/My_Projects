from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question


def index(request):
    questions = Question.objects.all()
    # res = ""
    # for q in questions:
    #     res += str(q.id) + ". " + q.question + "<br>"

    return render(request, "polls/index.html", {'question': question})


def detail(request, question_id):
    questions = get_object_or_404(Question, pk=question_id)
    # rez = "<H3>" + question.question + "<H3>: <br>"
    # for answer in question.choice_set.all():
    #     rez += answer.choice_text + " vote: " + str(answer.votes) + "<br>"
    return render(request, "polls/details.html", {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
