from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    pagnum=request.GET.get('page')
    pangnum=1 if pagnum == None else pagnum
    #排序，得到所有文章
    article=Article.objects.all().order_by('-views')
    paginator=Paginator(article,1)
    #传入页码得到页面，page包含所有信息
    page = paginator.get_page(pagnum)
    # page.object_list
    return render(request,'index.html',{'page':page})

def single(request,id):
    article=get_object_or_404(Article,pk=id)
    print(article)
    return render(request,'single.html',locals())