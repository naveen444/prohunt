from django.contrib import admin

from .models import Post, Postvote

admin.site.register(Post)

admin.site.register(Postvote)
