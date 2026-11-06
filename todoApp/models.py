from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=200)
    added_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    STATUS_CHOICES=(
    ('pending','pending'),
    ('completed','completed')
    )
    status=models.CharField(max_length=50,default="pending")

    def __str__(self):
        return self.title