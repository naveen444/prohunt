from django.contrib import admin

from .models import Post, Postvote, Comment, Commentvote, Commentdvote

admin.site.register(Post)

admin.site.register(Postvote)

admin.site.register(Comment)

admin.site.register(Commentvote)

admin.site.register(Commentdvote)
