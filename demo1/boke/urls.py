from django.conf.urls import url,include
from . import views
app_name='boke'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^single/(\d+)/$',views.single,name='single'),
]