from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    PUBLISHED_POSTS = 'Pub'
    DRAFT_POSTS = 'Drf'
    STATUS_CHOICES = [
        (PUBLISHED_POSTS,'Pub'),
        (DRAFT_POSTS,'Drf'),
    ]

    title = models.CharField(max_length=225)
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateField(auto_now=True)
    status = models.CharField(max_length=3,choices=STATUS_CHOICES,default=DRAFT_POSTS)


    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.pk])