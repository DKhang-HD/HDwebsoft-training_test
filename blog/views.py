# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import  render, get_object_or_404
from .models import Question, Choice
from django.http import Http404 
from django.urls import reverse

# def index(request):
#     latest_question_list = Question.objects.order_by ('-pub_date')[:5]
#     template = loader.get_template('blog/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     return HttpResponse(template.render(context,request))
    
# shortcut: render
def index(request):
    latest_question_list = Question.objects.order_by ('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'blog/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk =question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'blog/detail.html', {'question' : question})

# shortcut: get_object_or_404()
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'blog/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # 'choice' trong post được xác định bởi name = 'choice' trong input
                                                                            # giá trị của POST['choice'] xác định bởi value = "{{ choice.id }}"
    except (KeyError, Choice.DoesNotExist): 
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html', {'question': question})
    