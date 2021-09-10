from django.db import models

# Create your models here.

CATEGORY_CHOICES = [
    ('python', '파이썬'),
    ('web', '웹'),
    ('django', '장고'),
]

class Question(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'