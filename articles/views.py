from django.shortcuts import render
# model.py에서 db모델을 import한다

from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자가 form에서 전달한 정보를 꺼낸다. 
    # 해당 정보를 Article 모델을 이용하여 새롭게 데이터를 저장한다. 
    Article.objects.create(title=request.GET.get('title'), content=request.GET.get('content'))
    # articles = Article.objects.all()
    # context = {
    #     'articles': articles
    # }
    # 사용자에게 저장이 완료되었다는 페이지를 보여준다. 

    return render(request, 'articles/create.html')