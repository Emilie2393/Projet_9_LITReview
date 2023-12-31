from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
import authentication.views, bookblog.views
from django.conf import settings
from django.conf.urls.static import static
import bookblog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', bookblog.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('blog/my_posts', bookblog.views.my_posts, name='my_posts'),
    path('blog/create', bookblog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/askreview', bookblog.views.blog_and_photo_upload, name='ask_review'),
    path('blog/<int:blog_id>', bookblog.views.post_view, name='post_view'),
    path('blog/<int:blog_id>/edit', bookblog.views.edit_post, name='edit_blog'),
    path('blog/<int:blog_id>/review', bookblog.views.create_review, name='post_review'),
    path('blog/<int:review_id>/edit_review', bookblog.views.edit_review, name='edit_review'),
    path('follow-users/', bookblog.views.users_search, name='follow_users'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
