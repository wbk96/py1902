from django.conf.urls import url
from . import views
app_name='booktest'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^addbook/$',views.addbook,name='addbook'),
    url(r'^bookupdate/(\d+)/$',views.bookupdate,name='bookupdate'),
    url(r'^heroupdate/(\d+)$',views.heroupdate,name='heroupdate')
]