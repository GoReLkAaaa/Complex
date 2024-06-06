from django.contrib import admin
from .models import Profile, Publication, Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Publication)
admin.site.register(Comment)