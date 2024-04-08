# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# # Create your models here.
# class Notes(models.Model):
#     title=models.CharField(max_length=200)
#     text=models.TextField()
#     created=models.DateTimeField(auto_now_add=True)
#     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes')

# class Notes(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title    

from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


