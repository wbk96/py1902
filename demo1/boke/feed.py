


from django.contrib.syndication.views import Feed
from .models import *
from django.shortcuts import reverse

class BlogFeed(Feed):
    title='自我博客'
    description='记录每天的点点滴滴，轻松欢度每一天'
    link='/'

    def items(self):
        return Article.objects.all()

    def  item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:10]

    def item_link(self, item):
        return reverse('boke:single',args=(item.id,))