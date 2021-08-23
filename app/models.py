from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    foto_post=models.ImageField(upload_to='fotos_post/',blank=True)
    titulo= models.CharField(max_length=200)
    descripcion = models.CharField(max_length=700)
    created=models.DateTimeField(auto_now_add=True)


