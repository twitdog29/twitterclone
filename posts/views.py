from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm,PictureForm

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    # Get all posts, limit 20
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, "posts.html", {'posts': posts})
    
    
    # form = PostForm()
    #Show
    # return render(request,'index.html')
    # return render(request,'posts.html',
    #                 {'posts': posts})

            
def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def likes(request, post_id):
    newlikecount=Post.objects.get(id=post_id)
    #like_count.like = like_count + 1
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
        
    form = PostForm
    return render(request,'edit.html',{'post':post,'form':form})
        

def LoadPicture(request):
    return render (request, "load.html")