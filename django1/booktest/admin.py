from django.contrib import admin
from .models import BookInfo,HeroInfo
#路由
# Register your models here.

admin.site.register(BookInfo)
admin.site.register(HeroInfo)