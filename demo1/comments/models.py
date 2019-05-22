from django.db import models
from boke.models import Article
# Create your models here.

class Comment(models.Model):
    username=models.CharField(max_length=30)

    email=models.EmailField(blank=True,null=True)

    url=models.URLField(blank=True,null=True)

    # 评论
    content=models.CharField(max_length=500)

    article=models.ForeignKey(Article,on_delete=models.CASCADE)
