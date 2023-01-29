from django.shortcuts import render, redirect
from .models import photo, Post, BlogFile, Contact


def mulk(request):
    posts = photo.published.all()
    return render(request, 'blog/mulk.html', {'posts':posts})

def uy(request):
    return render(request, 'blog/uy.html')

def haqida(request):
    nams = Post.published.all()
    return render(request, 'blog/haqida.html', {'nams':nams} )


def BlogFiyle(request):
    texts = BlogFile.published.all()
    return render(request, 'blog/blogfile.html')


def aloqa(request):
    if request.method == "POST":
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(full_name=full_name, email=email, subject=subject, message=message)
        return redirect('uy')
    return render(request, 'blog/aloqa.html')

