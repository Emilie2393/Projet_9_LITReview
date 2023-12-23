from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from authentication import models as mod
from itertools import chain
from django.db.models import CharField, Value

# Create your views here.
@login_required
def home(request):
    tickets = models.Ticket.objects.filter(Q(user__in=request.user.follows.all()) | Q(user=request.user))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = models.Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    not_reviewed = []
    for ticket in tickets:
        review_flag = None
        for review in reviews:
            if review.ticket == ticket:
                review_flag = 1
        if review_flag is None:
            not_reviewed.append(ticket)
    posts = sorted(chain(reviews, tickets),
                    key=lambda post: post.time_created,
                    reverse=True
                    )
    context = {'posts': posts,
               'not_reviewed': not_reviewed}
    return render(request, 'bookblog/home.html', context=context)

@login_required
def blog_and_photo_upload(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.path != '/blog/askreview':
        context = {'review_form': review_form,
                   'blog_form': ticket_form}
    else:
        context = {'blog_form': ticket_form}
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.ticket = ticket
                review.user = request.user
                review.save()
            return redirect('home')
    return render(request, 'bookblog/create_post.html', context=context)

@login_required
def post_view(request, blog_id):
    blog = get_object_or_404(models.Ticket, id=blog_id)
    reviews = models.Review.objects.filter(Q(ticket=blog))
    context = {'author': blog.user,
               'user_online': request.user,
               'blog': blog,
               'reviews': reviews}
    return render(request, 'bookblog/post_view.html', context=context)

@login_required
def edit_post(request, blog_id):
    blog = get_object_or_404(models.Ticket, id=blog_id)
    edit_form = forms.TicketForm(instance=blog)
    post_review = forms.ReviewForm()
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_post' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_blog' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')
        if 'post_review' in request.POST:
            post_review = forms.ReviewForm(request.POST)
            if post_review.is_valid():
                review = post_review.save(commit=False)
                review.ticket = blog
                review.user = request.user
                review.save()
                return redirect("home")
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'post_review': post_review,
        'author': blog.user,
        'user_online': request.user}
    return render(request, 'bookblog/edit_post.html', context=context)

@login_required
def user_view(request, user_id):
    to_follow = get_object_or_404(mod.User, id=user_id)
    if request.method == 'POST':
        request.user.follows.add(to_follow)
        to_follow.followed_by.add(request.user)
        return redirect("follow_users")
    return render(request, 'bookblog/other_user_view.html', {'user_to_follow': to_follow})

@login_required
def users_search(request):
    followers = request.user.followed_by.all()
    follows = request.user.follows.all()
    context = {"followers": followers,
               "follows": follows}
    if request.method == 'POST':
        print(request.POST)
        if 'search' in request.POST:
            if request.POST['search'] != request.user.username:
                user_to_follow = mod.User.objects.get(Q(username=request.POST['search']))
                context = {"followers": followers,
                            "follows": follows,
                            "user_to_follow": user_to_follow}
        if 'data' in request.POST:
            request.user.follows.remove(mod.User.objects.get(Q(id=request.POST['data'])))
            mod.User.objects.get(Q(id=request.POST['data'])).followed_by.remove(request.user)

    return render(request, 'bookblog/follow_users.html', context)











