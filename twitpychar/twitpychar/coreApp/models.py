from django.db import models
from datetime import datetime

class Post(models.Model):
    content = models.TextField("Контент")
    postDate = models.DateTimeField("date", default=datetime.now)
    postImg = models.CharField("image", max_length=500, null=True, blank=True)

    #user/author = models.ForeignKey(User)
    def __str__(self):
        return f"post user {self.pk}"
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"