from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import HeroInfo,BookInfo
# Create your views here.
# mvt 中的 v

def index(request):
    # return HttpResponse('index首页')
    temp=loader.get_template('booktest/index.html')
    result=temp.render({})
    return HttpResponse(result)


def list(request):
    # return HttpResponse('列表页')
    allbook=BookInfo.objects.all()
    temp = loader.get_template('booktest/list.html')
    result = temp.render({'allbook':allbook})
    return HttpResponse(result)


def detail(request,id):
    print(id)
    # return HttpResponse('详情页')
    book=None
    try:
        book=BookInfo.objects.get(pk=id)
    except Exception as e:
        return "书籍不存在"
    temp = loader.get_template('booktest/detail.html')
    result = temp.render({'book':book})
    return HttpResponse(result)
# list('request')

def deletebook(request,id):
    # return HttpResponse('SUCCESS')
    BookInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')

def deletehero(request,id):
    # return HttpResponse('SUCCESS')
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return HttpResponseRedirect('/booktest/detail/%s'%bookid)

def addhero(request,id):
    if request.method == "GET":
        print('get')
        return render(request,'booktest/addhero.html',{'bookid':id})
    elif request.method =='POST':
        print('post')
        book=BookInfo.objects.get(pk=id)
        hero=HeroInfo()
        hero.name= request.POST['heroname']
        hero.gender=request.POST['sex']
        hero.skill=request.POST['skill']
        hero.book=book
        hero.save()
        return HttpResponseRedirect('/booktest/detail/%s'%id)
def addbook(request):
    if request.method=='GET':
        return render(request, 'booktest/addbook.html')
    elif request.method=='POST':
        book=BookInfo()
        book.title=request.POST['bookname']
        book.bpud_data=request.POST['time']
        book.save()
        return HttpResponseRedirect('/booktest/list/')

def bookupdate(request,id):
    book = BookInfo.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'booktest/bookupdate.html',{'book':book})
    elif request.method=='POST':
        book.title=request.POST['bookname']
        book.bpud_data=request.POST['time']
        book.save()
        return HttpResponseRedirect('/booktest/list/')

def heroupdate(request,id):
    hero = HeroInfo.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'booktest/heroupdate.html',{"hero":hero})
    elif request.method=='POST':
        bookid=hero.book.id
        hero.name=request.POST['heroname']
        hero.gender=request.POST['sex']
        hero.skill=request.POST['skill']
        hero.save()
        return HttpResponseRedirect('/booktest/detail/%s'%bookid)
