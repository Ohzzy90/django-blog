from django.shortcuts import render, redirect

from usermanager.models import Comment
from .forms import Postform
# Create your views
from .models import BlogDb
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required
def index(request):
    blogpost=BlogDb.objects.all().order_by("-postdate")
    page=Paginator(blogpost,2)
    page_context=request.GET.get("page")
    page_view=page.get_page(page_context)

    # blogpost=[{
    #          "blogtitle":"Bible Society",
    #          "blogcontent":"Fear of God is the beginning of wisdom to differentiate between Good and Evil",
    #          "blogauthor":"Jim Chris",
    #          "postdate":datetime.today(),
    #          "image":"Morales.jpg"
    #          },

    #          {"blogtitle":"Bible Society",
    #         "blogcontent":"Fear of God is the beginning of wisdom to differentiate between Good and Evil",
    #         "blogauthor":"Baryl Authur",
    #         "postdate":datetime.today(),
    #         "image":"Morales.jpg"
    #         },

    #         ]

    message='<h1>Welcome to Blogger</h1>'
    return render(request,"blogs/index.html",{"blogpost":blogpost, "msg":message, "page_view":page_view})

@login_required()
def Post(request):
    if request.method=="POST":
        New_post=Postform(request.POST, request.FILES)
        if New_post.is_valid():
            New_post.save()
            return redirect("/")
    else:
        New_post=Postform()
    return render(request,"blogs/newpost.html", {"New_post":New_post})

@login_required
def EditDetails(request, id):
    editpost=BlogDb.objects.get(pk=id)
    if request.method=="POST":
        editform=Postform(request.POST, request.FILES, instance=editpost)
        if editform.is_valid():
            editform.save()
            return redirect("/")
    else:
        editform=Postform(instance=editpost)
    return render(request,"blogs/edit.html",{"editform":editform})


def DetailPost(request, id):
    postinfo=BlogDb.objects.get(pk=id)
    no_comment=Comment.objects.filter(blog=postinfo
    ).count()
    return render(request,"blogs/details.html", {"postinfo":postinfo,"no_comment":no_comment})

@login_required
def deletepost(request, id):
    delpost=BlogDb.objects.get(pk=id)
    delpostid=delpost.id
    if request.method=="POST":

        delpost.delete()
        return redirect("/")
    else:
        return render(request, "blogs/delete.html", {"pid":delpostid})








