from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    user_post = models.TextField(verbose_name='текст поста')
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
