from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from authentication import models as mod

# Create your views here.
@login_required
def home(request):
    photos = models.Photo.objects.all()
    blogs = models.Blog.objects.all()
    """filter(Q(author=request.user) & Q(users__in=request.user.follows.all()))
    print(models.Blog.objects.all()[0].author)"""
    context = {'blogs': blogs}
    return render(request, 'bookblog/home.html', context=context)

@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            blog.users.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
        }
    return render(request, 'bookblog/create_post.html', context=context)


@login_required
def post_view(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'bookblog/post_view.html', {'blog': blog})

@login_required
def edit_post(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_blog' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }
    return render(request, 'bookblog/edit_post.html', context=context)

"""@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'bookblog/follow_users.html', context={'form': form})"""

@login_required
def users_search(request):
    context = {}
    if request.method == 'POST':
        name = request.POST
        if name is not None:
            if 'search' in name:
                print("coucou")
                if name['search'] != request.user.username:
                    user = mod.User.objects.get(username=name['search'])
                    context = {
                        'username': user
                    }
            else:
                print("pas search")
    return render(request, 'bookblog/follow_users.html', context)



