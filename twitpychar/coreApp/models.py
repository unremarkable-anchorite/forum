from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Post(models.Model):
    content = models.TextField("Контент")
    postDate = models.DateTimeField("date", default=datetime.now)
    postImg = models.CharField("image", max_length=500, null=True, blank=True)
    userPost = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Post by", default="")
    #user/author = models.ForeignKey(User)
    def __str__(self):
        return f"post user #{self.pk}"

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"