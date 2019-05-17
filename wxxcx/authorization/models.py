from django.db import models

# Create your models here.


class User(models.Model):
    #微信open_id
    open_id = models.CharField(max_length=32, unique=True)
    #昵称
    nickname = models.CharField(max_length=256)