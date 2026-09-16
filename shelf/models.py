from django.db import models


# Create your models here.


class Book(models.Model):
  STATUS_CHOICES = [
      ("want", "Want to Read"),
      ("reading", "Currently Reading"),
      ("read", "Finished"),
  ]
  
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  description = models.TextField()
  isbn = models.CharField(max_length=13)
  # cover = models.ImageField(upload_to='covers/', blank=True, null=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="want")
  published_at = models.DateField(blank=True, null=True, auto_now_add=True)
  updated_at = models.DateField(blank=True, null=True, auto_now=True)
  
  
  # ordering = ['-published_at']
  
  def __str__(self):
    return self.title[:50]