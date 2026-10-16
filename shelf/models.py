from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
class Book(models.Model):
  STATUS_CHOICES = [
      ("want", "Want to Read"),
      ("reading", "Currently Reading"),
      ("read", "Finished"),
  ]
  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  description = models.TextField()
  book_cover = models.ImageField(upload_to='book_covers/', blank=True, null=True, default='book_covers/default_cover.png')
  isbn = models.CharField(max_length=13)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="want")
  published_at = models.DateField(blank=True, null=True, auto_now_add=True)
  updated_at = models.DateField(blank=True, null=True, auto_now=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
  
  class Meta:
    ordering = ['-published_at']
  
  def __str__(self):
    return self.title[:50]
  