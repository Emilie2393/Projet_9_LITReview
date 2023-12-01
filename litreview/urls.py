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
    path('photo/upload/', bookblog.views.photo_upload, name='photo_upload')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
