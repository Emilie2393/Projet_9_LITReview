from django.contrib import admin
from django.urls import path
import authentication.views, bookblog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', bookblog.views.home, name='home'),
]
