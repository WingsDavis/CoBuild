from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    
       
    def __str__(self):
        return self.name    

class Project(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
       
    def __str__(self):
        return self.body[0:100]


    
    