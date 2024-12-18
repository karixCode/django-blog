from symtable import Class

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name='Имя')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    bio = models.TextField(verbose_name='Биография')

    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, verbose_name='Лайки')

    def __str__(self):
        return f"Пост {self.id} от {self.author.username}"

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comment_set.count()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий {self.id} от {self.author.username}"