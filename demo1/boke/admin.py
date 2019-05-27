from django.contrib import admin
from .models import Article,Tag,Category,MessageInfo,Ads

# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(MessageInfo)
admin.site.register(Ads)