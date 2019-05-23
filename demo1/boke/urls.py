from django.conf.urls import url,include
from . import views,feed
app_name='boke'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^archives/(\d+)/(\d+)/$',views.archives,name='archives'),
    url(r'^category/(\d+)/$',views.category,name='category'),
    url(r'^catetag/(\d+)/$',views.catetag,name='catetag'),
    url(r'^rss/$',feed.BlogFeed(),name='rss'),
    url(r'contactus/$',views.contactus,name='contactus'),
    url(r'^single/(\d+)/$',views.single,name='single'),
]