from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_object(self):
        question_text = self.kwargs.get("question_text")
        return get_object_or_404(Question, question_text=question_text)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.question_text == 'favactor':
            context['choices'] = self.object.choice_set.order_by('choice_text')
        else:
            context['choices'] = self.object.choice_set.order_by('-id')
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_object(self):
        question_text = self.kwargs.get("question_text")
        return get_object_or_404(Question, question_text=question_text)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.question_text == 'fav actor':
            context['choices'] = self.object.choice_set.order_by('choice_text')
        else:
            context['choices'] = self.object.choice_set.order_by('-id')
        return context


def vote(request, question_text):
    question = get_object_or_404(Question, question_text=question_text)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with choices ordered alphabetically.
        return render(request, 'polls/detail.html', {
            'question': question,
            'choices': question.choice_set.order_by('choice_text'),
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.question_text,)))


def results(request, question_text):
    question = get_object_or_404(Question, question_text=question_text)
    return render(request, 'polls/results.html', {
        'question': question,
        'choices': question.choice_set.order_by('choice_text'),
    })
