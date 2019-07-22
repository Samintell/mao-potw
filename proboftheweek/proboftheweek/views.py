from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Question, Response


def index(request):
    now = datetime.now()

    return render(
        request,
        "proboftheweek/index.html", 
        {
            'title': 'testme',
            'message': 'sanity check'
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
    for q in Question.objects.all():
        if (now.day == q.active_date.day) and (now.month == q.active_date.month) and (now.year == q.active_date.year) and (now.hour >= 18):
            return render(
                request,
                "proboftheweek/active.html", 
                {
                    'act': True,
                    'act_question': q
                })
    return render(
            request,
            "proboftheweek/active.html", 
            {
                'act': False,
            })

def submit_ans(request):
    try:
        q = get_object_or_404(Question, pk=request.POST['q_id'])
    except:
        return render(request, 'proboftheweek/index.html', {
                'error_message': "Illegal Request",
            })
    try:
        if request.POST['student_id'] == '':
            return render(request, 'proboftheweek/active.html', {
                'error_message': "You didn't provide Student ID",
                'act_question': q,
                'act': True
            })
        elif request.POST['answer'] == '':
            return render(request, 'proboftheweek/active.html', {
                'error_message': "You didn't provide an answer",
                'act_question': q,
                'act': True
            })
        r = Response(question = q, student_id = request.POST['student_id'].strip(), answer_text=request.POST['answer'].strip())
    except (KeyError):
        return render(request, 'proboftheweek/active.html', {
            'error_message': "Invalid Submission",
        })
    else:
        r.save()
        return HttpResponseRedirect('../home/')



    
