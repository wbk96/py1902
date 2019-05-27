from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
import markdown
from comments.forms import comment
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from django.views import View
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

    if request.method=='GET':
        return render(request,'contact.html')
    elif request.method=='POST':
        try:
            send_mail('测试邮件', '测试用的', settings.DEFAULT_FROM_EMAIL, ['1774678547@qq.com', ])
        except Exception as e:
            print(e)
        return redirect(reverse('boke:contactus'))

class addimg(View):
    print('走过没')
    def get(self,request):
        return render(request,'addimg.html')
    def post(self,request):
        try:
            img=request.FILES['img']
            desc=request.POST.get('desc')
            ad=Ads(img=img,desc=desc)
            ad.save()
            return redirect(reverse('boke:index'))
        except Exception as e:
            return redirect(reverse('boke:addimg'),{'error':'未添加成功'})



