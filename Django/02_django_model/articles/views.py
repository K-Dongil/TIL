import articles
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # 1. 모든 게시글 조회
    articles = Article.objects.all()
    print(articles)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new로부터 title과 content를 받아서 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 2
    article = Article(title = title, content = content)
    article.save()
    # 3
    # Article.objects.create(title = title, content = content)
    return render(request, 'articles/create.html')


def detail(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles':articles
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method  == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('article:detail', article.pk)