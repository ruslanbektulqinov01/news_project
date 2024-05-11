from django.shortcuts import render, get_object_or_404, redirect
from .models import Artice, Comment, Like
from django.contrib.auth.decorators import login_required


# @login_required
def article(request):
    articles = Artice.objects.all().order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'articles': articles
    }
    return render(
        request=request,
        template_name='home.html',
        context=context
    )


# @login_required
def world_news(request):
    articles = Artice.objects.filter(tag='world').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'articles': articles
    }
    return render(
        request=request,
        template_name='home.html',
        context=context
    )


# @login_required
def local_news(request):
    articles = Artice.objects.filter(tag='local').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'articles': articles
    }
    return render(
        request=request,
        template_name='home.html',
        context=context
    )


# @login_required
def sports_news(request):
    articles = Artice.objects.filter(tag='sport').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'articles': articles
    }
    return render(
        request=request,
        template_name='home.html',
        context=context,
    )

# @login_required()
def article_detail(request, id):
    article = get_object_or_404(Artice, id=id)
    comments = Comment.objects.filter(article_id=id)
    likes = Like.objects.filter(article_id=id)
    context = {
        "article": article,
        "comments": comments,
        "likes": likes
    }

    if request.method == 'POST':
        if 'comment' in request.POST:
            Comment.objects.create(user_id=request.user, article_id=article, text=request.POST['comment'])
        elif 'like' in request.POST:
            Like.objects.create(user_id=request.user, article_id=article, like=True, dislike=False)
        elif 'dislike' in request.POST:
            Like.objects.create(user_id=request.user, article_id=article, like=False, dislike=True)
        return redirect('article_detail', id=id)

    return render(
        request=request,
        template_name='article_detail.html',
        context=context,
    )
