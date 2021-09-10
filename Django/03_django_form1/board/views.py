from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .forms import QuestionForm
from django.views.decorators .http import require_safe, require_POST, require_http_methods
from django.core.paginator import Paginator

# Create your views here.

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['is_save']:
                question = form.save() # model의 instance가 return된다
                return redirect('board:detail', question.pk)
            else:
                return redirect('board:create')
    else:
        form = QuestionForm()

    context = {'form':form}
    return render(request, 'board/form.html', context)

@require_safe
def index(request):
    questions = Question.objects.order_by('-pk')

    paginator = Paginator(questions, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'board/index.html', context)

@require_safe
def detail(request, question_pk):
    question =  get_object_or_404(Question, pk=question_pk)
    context = {
        'question': question,
    }
    return render(request, 'board/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, question_pk):
    question =  get_object_or_404(Question, pk=question_pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save() # model의 instance가 return된다
            return redirect('board:detail', question.pk)   
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'board/form.html', context)

@require_POST
def delete(request, question_pk):
    question =  get_object_or_404(Question, pk=question_pk)
    question.delete()
    return redirect('board:index')