from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Question, Response
from django.utils import timezone
from django.views import generic
import pytz


def index(request):
    now = datetime.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            'title': "OTHS MAO",
            'error': False,
        })

def test(request):
    now = datetime.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            
        })

def weekly(request):
    now = datetime.now()
    print(now.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
    print(datetime.now())
    for q in Question.objects.all():
        if (now.day == q.active_date.day) and (now.month == q.active_date.month) and (now.year == q.active_date.year) and (now.hour == 18) and (now.minute < 15):
            return render(
                request,
                "proboftheweek/active.html", 
                {
                    'title':"Active",
                    'act': True,
                    'act_question': q
                })
    return answer(request)

def submit_ans(request):
    now = datetime.now()
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
        r = Response(question = q, student_id = request.POST['student_id'].strip(), answer_text=request.POST['answer'].strip(), time=now)
    except (KeyError):
        return render(request, 'proboftheweek/active.html', {
            'title':"Error",
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
        active_date__lt=datetime.now().date()
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
                'title': "Archive",
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

def success(request):
    return render(request, 'proboftheweek/success.html', {
                'title': "Success",
            }) 

def answer(request):
    now = datetime.now()
    print(now.strftime("%d-%b-%Y (%H:%M:%S.%f)"))
    for q in Question.objects.all():
        if (now.day == q.active_date.day) and (now.month == q.active_date.month) and (now.year == q.active_date.year) and (now.hour >= 18) :
            if datetime(now.year, now.month, now.day, 6, 15) < now:
                return render(
                    request,
                    "proboftheweek/archived_q.html", 
                    {
                        'title': q.active_date,
                        'q': q
                    })
    return render(
            request,
            "proboftheweek/index.html", 
            {
                'title': "OTHS MAO",
                'error': True,
                'error_message': "Question not available",
            })

class QListView(generic.ListView):
    template_name = 'proboftheweek/qlist.html'
    context_object_name = 'questions_list'

    def get_queryset(self):
        return Question.objects.order_by('-active_date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "questions"
        return context

class ResponsesView(generic.ListView):
    template_name = 'proboftheweek/responses.html'
    context_object_name = 'responses_list'

    def get_queryset(self):
        return Response.objects.filter(question__id=self.kwargs['question_id']).order_by('time')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "responses"
        context['answer'] = get_object_or_404(Question, pk=self.kwargs['question_id']).answer
        return context
