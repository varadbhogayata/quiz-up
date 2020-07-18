from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import QuizProfile, Question, AttemptedQuestion


# Create your views here.
def index(request):
    return render(request, 'quiz/index.html', context=None)


@login_required(login_url='login')
def user_home(request):
    return render(request, 'quiz/user_home.html', context=None)


def leaderboard(request):
    top_quiz_profiles = QuizProfile.objects.order_by('-total_score')[:500]
    total_count = top_quiz_profiles.count()
    context = {
        'top_quiz_profiles': top_quiz_profiles,
        'total_count': total_count,
    }
    return render(request, 'quiz/leaderboard.html', context=context)


@login_required(login_url='login')
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')

        attempted_question = quiz_profile.attempts.select_related('question').get(question__pk=question_pk)

        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = attempted_question.question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        quiz_profile.evaluate_attempt(attempted_question, selected_choice)

        return redirect(attempted_question)

    else:
        question = quiz_profile.get_new_question()
        if question is not None:
            quiz_profile.create_attempt(question)

        context = {
            'question': question,
        }

        return render(request, 'quiz/play.html', context=context)


@login_required(login_url='login')
def submission_result(request, attempted_question_pk):
    attempted_question = get_object_or_404(AttemptedQuestion, pk=attempted_question_pk)
    context = {
        'attempted_question': attempted_question,
    }

    return render(request, 'quiz/submission_result.html', context=context)


def error_404(request):
    return render(request, 'quiz/error_404.html', context=None)


def error_500(request):
    return render(request, 'quiz/error_500.html', context=None)
