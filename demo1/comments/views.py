from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Comment
from django.views.generic import View
# Create your views here.
from .models import Article
from .models import Comment
from django.http import HttpResponse
class AddComment(View):
    def post(self,request,id):
        article=get_object_or_404(Article,pk=id)

        username=request.POST.get('name')
        email=request.POST.get('email')
        url=request.POST.get('url')
        comment=request.POST.get('comment')

        c=Comment()
        c.username = username
        c.email=email
        c.url=url
        c.content=comment
        c.article=article
        c.save()
        return redirect(reverse('boke:single',args=(id,)))