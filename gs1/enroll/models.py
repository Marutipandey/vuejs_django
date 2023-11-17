# models.py
from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    todo_name = models.CharField(max_length=100)
    is_created = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_todos")

    
