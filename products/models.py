from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#product class
class Product(models.Model):
    title = models.CharField(max_length = 50)   #title
    product_description = models.TextField(max_length = 120, default='', null=True, blank=True)
    product_summary = RichTextField()  # body
    url = models.TextField(default='', null=True, blank=True)   #url
    icon = models.ImageField(upload_to = 'images/')     #icon
    image = models.ImageField(upload_to = 'images/')    # image
    pub_date = models.DateTimeField()   # pub_date
    votes_total = models.IntegerField(default = 1)
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')   # pub_date_pretty

class Vote(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
