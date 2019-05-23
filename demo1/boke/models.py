from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

#分类模型
class Category(models.Model):
    title = models.CharField(max_length=30,verbose_name='类型')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name='类型'
        verbose_name_plural=verbose_name

# 标签模型
class Tag(models.Model):
    title = models.CharField(max_length=30,verbose_name='标签')
    def __str__(self):
        return self.title
    class Meta():
        verbose_name='标签'
        verbose_name_plural=verbose_name
# 文章模型
class Article(models.Model):
    title=models.CharField(max_length=30,verbose_name='文章')
    body=models.TextField()
    creater_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    views=models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    auth = models.ForeignKey(User,models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name='文章'
        verbose_name_plural=verbose_name



class MessageInfo(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(blank=Tag,null=True)
    subject =models.CharField(max_length=50)
    #非Django原生类型
    info=HTMLField()


