from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    email = models.EmailField(default="", ) #추가했는데 에러 뜸??? 뭐 다른 걸 설정해야하나...
    createdAt = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title 

#4일차 과제 관련..
    

# create your models here.