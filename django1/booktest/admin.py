from django.contrib import admin
from .models import BookInfo,HeroInfo
#路由
# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    #关联个数
    extra = 1
class BookInfoadmin(admin.ModelAdmin):
    list_display = ['title','bpud_data']
    list_filter = ['title','bpud_data']
    search_fields = ['title','bpud_data']
    inlines = [HeroInfoInline]

class HeroInfoadmin(admin.ModelAdmin):
    list_display = ['name','gender']
    list_filter = ['name','gender']
    search_fields = ['name','gender']

admin.site.register(BookInfo,BookInfoadmin)
admin.site.register(HeroInfo,HeroInfoadmin)