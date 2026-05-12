from webbrowser import get
from django.urls import reverse
from django.shortcuts import render, redirect
from blogs.models import BlogDb

from usermanager.models import Comment, Like, ProfileModel
from .forms import Newuserform,Profileform,Edituserform, commentform,likeform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_user(request):
    if request.method=="POST":
        userform=Newuserform(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request, "Registration Successfully")
            return redirect("/")
    else:
        userform=Newuserform()
    return render(request, "usermanager/register.html", {"userform":userform})  

def login_request(request):
    if request.method=="POST":
        loginform=AuthenticationForm(request,request.POST)
        if loginform.is_valid():
            usern=loginform.cleaned_data.get("username")
            passw=loginform.cleaned_data.get("password")
            myuser=authenticate(request,username=usern,password=passw)
            if myuser is not None:
                login(request, myuser)
                return redirect("Home")
    else:
        loginform=AuthenticationForm()
    return render(request, "usermanager/login.html", {"loginform":loginform})  

def logout_request(request):
    logout(request)
    messages.info(request, f'you have been logged out successfully')
    return redirect ('Home')   

def profilemanager(request):
    uins=ProfileModel.objects.get(user=request.user)
    if request.method=="POST":
        euform=Edituserform(request.POST,instance=request.user)
        pform=Profileform(request.POST,request.FILES, instance=uins)
        if pform.is_valid() and euform.is_valid():
            pform.save()
            euform.save()
            return redirect(reverse('profile'))
    else:
        euform=Edituserform(instance=request.user)
        pform=Profileform(instance=uins)
    return render(request, "usermanager/profile.html", {"pform":pform,"euform":euform})

@login_required()
def commentbox(request,id):
    blog=BlogDb.objects.get(pk=id)
    # cf=commentform(instance=blog)
    if request.method=="POST":
        cf=commentform(request.POST,instance=blog)
        if cf.is_valid():
            author=request.user
            content=cf.cleaned_data.get("content")
            comment=Comment(blog=blog,author=author,content=content)
            comment.save()
            return redirect(reverse('details',kwargs={"id":id}))
            # return redirect("/")
    else:
        cf=commentform()
    return render(request,"usermanager/comment.html",{"cf":cf})

def reaction(request):
    blog=BlogDb.objects.get(pk=id)
    if request.method=="POST":
        lk=likeform(request.POST,instance=blog)
        if lk.is_valid():
            author=request.user
            react=lk.cleaned_data.get("react")
            liking=Like(blog=blog,author=author,react=react)
            liking.save()
            return redirect(reverse('details', kwargs={"id":id}))
    else:
        lk=likeform()
    return render(request, "usermanager/likes.html", {"lk":lk})


def del_comment(request,id):
    del_com=Comment.objects.get(pk=id)
    detail_id=del_com.blog.id
    del_com.delete()
    return redirect(reverse('details', args=[detail_id]))
