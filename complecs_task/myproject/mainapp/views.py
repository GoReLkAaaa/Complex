from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Comment, Profile, Publication
from django.core.paginator import Paginator
from django.http import  HttpResponse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        templates = 'mainapp/index.html'
        context = {
            'user': request.user
        }
        return render(request, templates, context)
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'GET':
        templates = 'mainapp/login.html'
        return render(request, templates)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')



def register(request):
    if request.method == 'GET':
        templates = 'mainapp/register.html'
        return render(request, templates)
    else:
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')



def logout_view(request):
    logout(request)
    return redirect('login')


def icon(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            templates = 'mainapp/icon.html'
            return render(request, templates)
        else:
            icon = request.FILES['icon']
            profile = Profile(icon=icon, user_id=id)
            profile.save()
            return redirect('index')
    else:
        return redirect('login')


def publications(request):
    if request.user.is_authenticated:
        templates = 'mainapp/publications.html'
        paginator = Paginator(Publication.objects.all(), 3)
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        publication = paginator.page(page)
        context = {
            'publications': publication,
            'paginator': paginator
        }
        return render(request, templates, context)
    else:
        return redirect('login')


def detail(request, id):
    if request.user.is_authenticated:
        templates = 'mainapp/detail.html'
        paginator = Paginator(Comment.objects.filter(publications_id=id), 2)
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        comment = paginator.page(page)
        context = {
            'publications': Publication.objects.get(id=id),
            'comments': comment,
            'paginator': paginator
        }
        return render(request, templates, context)
    else:
        return redirect('login')


def delete_comment(request, id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=id)
        if comment.user == request.user:
            comment.delete()
            return redirect('publications')
        else:
            return HttpResponse('Вы не являетесь автором коммента, нельзя удалить')
    else:
        return redirect('login')


def create_comment(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            templates = 'mainapp/create_comment.html'
            context = {
                'publication': Publication.objects.get(id=id)
            }
            return render(request, templates, context)
        else:
            name = request.POST['name']
            comment = Comment(name=name, user_id=request.user.id, publications_id=id)
            comment.save()
            return redirect('detail', int(id))
    else:
        return redirect('login')



def create_publications(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            templates = 'mainapp/create_post.html'
            return render(request, templates)
        else:
            name = request.POST['name']
            image = request.FILES['image']
            publication = Publication(name=name, image=image, user_id=request.user.id)
            publication.save()
            return redirect('publications')
    else:
        return redirect('login')


def update(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            templates = 'mainapp/update_post.html'
            context = {
                'publications': Publication.objects.get(id=id)
            }
            return render(request, templates, context)
        else:
            name = request.POST['name']
            image = request.FILES['image']
            publication = Publication.objects.get(id=id)
            if publication.user == request.user:
                publication = Publication(name=name, image=image, id=id, user_id=request.user.id)
                publication.save()
                return redirect('publications')
            else:
                return HttpResponse('Нельзя обновить')
    else:
        return redirect('login')