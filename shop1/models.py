from django.db import models
from django.contrib.auth.models import User

class Index(models.Model):
    title = models.CharField(max_length=200, db_index=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    index = models.ForeignKey(Index, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.PROTECT, related_name='comments', null=True)
    name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']









