from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Question, Response
from django.utils import timezone
from django.views import generic


def index(request):
    now = timezone.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            'title': "OTHS MAO",
            'error': False,
        })

def test(request):
    now = timezone.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            
        })

def weekly(request):
    now = timezone.now()
    for q in Question.objects.all():
        if (now.day == q.active_date.day) and (now.month == q.active_date.month) and (now.year == q.active_date.year) and (now.hour >= 18) and now.minute <= 15:
            return render(
                request,
                "proboftheweek/active.html", 
                {
                    'title':"Active",
                    'act': True,
                    'act_question': q
                })
    return render(
            request,
            "proboftheweek/active.html", 
            {
                'title': "Inactive.",
                'act': False,
                'error': False,
            })

def submit_ans(request):
    try:
        q = get_object_or_404(Question, pk=request.POST['q_id'])
    except:
        return render(request, 'proboftheweek/index.html', {
                'title': "OTHS MAO",
                'error_message': "Illegal Request",
                'error':True
            })
    try:
        if request.POST['student_id'] == '':
            return render(request, 'proboftheweek/active.html', {
                'title':"Active",
                'error_message': "You didn't provide Student ID",
                'act_question': q,
                'act': True,
                'error':True
            })
        elif request.POST['answer'] == '':
            return render(request, 'proboftheweek/active.html', {
                'title':"Active",
                'error_message': "You didn't provide an answer",
                'act_question': q,
                'act': True,
                'error':True
            })
        r = Response(question = q, student_id = request.POST['student_id'].strip(), answer_text=request.POST['answer'].strip())
    except (KeyError):
        return render(request, 'proboftheweek/active.html', {
            'error_message': "Invalid Submission",
            'error':True
        })
    else:
        r.save()
        return HttpResponseRedirect('../home/')

class ArchiveView(generic.ListView):
    template_name = 'proboftheweek/archive.html'
    context_object_name = 'past_questions_list'

    def get_queryset(self):
        return Question.objects.filter(
        active_date__lt=timezone.now().date()
        ).order_by('-active_date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Archive"
        return context

def arch_q(request, question_id):
    try:
        q = get_object_or_404(Question, pk=question_id)
    except:
        return render(request, 'proboftheweek/archive.html', {
                'error_message': "Illegal Request",
                'title': "Archiive",
                'error':True
            }) 
    if (q.active_date < timezone.now().date()):
        return render(request, 'proboftheweek/archived_q.html', {
                'q':q,
                'title': q.active_date,
            })
    else:
        return render(request, 'proboftheweek/archive.html', {
                'error':True,
                'error_message': "Question not available",
                'title': "OTHS MAO",
            }) 



    
