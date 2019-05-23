from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
import markdown
from comments.forms import comment
# Create your views here.


def index(request):
    pagnum=request.GET.get('page')
    pagnum=1 if pagnum == None else pagnum
    #排序，得到所有文章
    article=Article.objects.all().order_by('-views')
    paginator=Paginator(article,1)
    #传入页码得到页面，page包含所有信息
    page = paginator.get_page(pagnum)

    return render(request,'index.html',{'page':page})

def single(request,id):
    article=get_object_or_404(Article,pk=id)
    article.views+=1
    article.save()
    #使用markdown处理body，将markdown语法转换为html标签

    #第一种使用，针对需要处理的article.body 将markdown转换为html语法
    # article.body = markdown.markdown(article.body,extensions = [
    #         "markdown.extensions.extra",
    #         "markdown.extensions.codehilite",
    #         "markdown.extensions.toc",]）
  #第二种如果在外部目录使用 需要使用构造函数的写法
    mk=markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc",])
    article.body=mk.convert(article.body)
    #将markdown中的目录赋于article的toc对象
    article.toc = mk.toc
    cf = comment()
    return render(request,'single.html',locals())

def archives(request,year,month):
    article=Article.objects.filter(creater_time__year=year,creater_time__month=month)
    paginator = Paginator(article, 1)
    # 传入页码得到页面，page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})
#分类显示
def category(request,id):
    article=get_object_or_404(Category,pk=id).article_set.all()
    paginator = Paginator(article, 1)
    # 传入页码得到页面，page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})

def catetag(request,id):
    article = get_object_or_404(Tag, pk=id).article_set.all()
    paginator = Paginator(article, 1)
    # 传入页码得到页面，page包含所有信息
    page = paginator.get_page(1)
    return render(request, 'index.html', {'page': page})

def contactus(request):
    return render(request,'contact.html')


