from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #CharField에는 항상 max_length를 설정해야함
    content = models.TextField()

# 여기까지가 모델을 정의한 것