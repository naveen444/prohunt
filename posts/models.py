from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    post_summary = RichTextField(null=True, blank=True)  # body
    url = models.TextField(default='', null=True, blank=True)   #url
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)    # image
    pub_date = models.DateTimeField()   # pub_date
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    votes_total = models.IntegerField(default = 0)
    total_comments = models.IntegerField(default = 0)
    
    def postsummary(self):
        return self.post_summary[:300]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')   # pub_date_pretty

class Postvote(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_text = RichTextField()
    comment_pub_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    votes_total = models.IntegerField(default = 0)


    def postsummary(self):
        return self.post_summary[:300]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')

class Commentvote(models.Model):
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
