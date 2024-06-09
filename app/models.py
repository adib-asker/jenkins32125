from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
