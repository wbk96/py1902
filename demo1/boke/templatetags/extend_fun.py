from django import template
from ..models import *
register=template.Library()

@register.filter(name='myslice')
def myslice(value,lenth):
    return value[:lenth]

@register.simple_tag
def getlastartice(num=3):
       return Article.objects.all().order_by('-creater_time')[:num]

@register.simple_tag
def getlastmous(num=3):
    return Article.objects.dates('creater_time','month',order='DESC')[:num]

@register.simple_tag
def getleifen():
    return Category.objects.all()

@register.simple_tag
def gettag():
    return  Tag.objects.all()

@register.simple_tag
def getads():
    return Ads.objects.all()
