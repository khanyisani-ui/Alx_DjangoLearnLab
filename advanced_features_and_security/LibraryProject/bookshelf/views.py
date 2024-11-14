from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article

@login_required
@permission_required('yourapp.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'yourapp/article_list.html', {'articles': articles})

@login_required
@permission_required('yourapp.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # Handle article creation logic
        pass
    return render(request, 'yourapp/article_form.html')

@login_required
@permission_required('yourapp.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Handle article editing logic
        pass
    return render(request, 'yourapp/article_form.html', {'article': article})

@login_required
@permission_required('yourapp.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'yourapp/article_confirm_delete.html', {'article': article})
