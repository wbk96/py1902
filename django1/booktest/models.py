from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title=models.CharField(max_length=30,verbose_name='书名')
    bpud_data=models.DateTimeField(auto_now_add=True,verbose_name='出版日期')
    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name='英雄名')
    gender=models.CharField(max_length=10,choices=(('man','男'),('women','女')))
    skill=models.CharField(max_length=30,blank=True,null=True,verbose_name='技能')
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='书名')
    def __str__(self):
        return self.name

class modelext(models.Manager):
    def createone(self,_title):
        t=self.model()
        t.tel=_title
        t.save()
    def getone(self,_title):
        self.createone(_title)
        return


class tel(models.Model):
    tel=models.CharField(max_length=20)
    #添加字段   字段为模型管理器
    # manager=models.Manager()
    objects= modelext()
    @classmethod
    def create(cls,_title):
        t=cls(tel=_title)
        t.save()




