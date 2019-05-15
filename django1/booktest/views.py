from django.shortcuts import render
from django.http import HttpResponse
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