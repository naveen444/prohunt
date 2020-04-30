from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    post_summary = RichTextField()  # body
    url = models.TextField(default='', null=True, blank=True)   #url
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)    # image
    pub_date = models.DateTimeField()   # pub_date
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    votes_total = models.IntegerField(default = 0)

    def postsummary(self):
        return self.post_summary[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')   # pub_date_pretty

class Postvote(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
