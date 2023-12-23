from django.contrib import admin
from bookblog.models import Ticket, Review
from authentication.models import User

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(User)

# Register your models here.
