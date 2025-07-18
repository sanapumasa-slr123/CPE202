# CPE202/models.py (Example)
from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields as needed for your portfolio items
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields as needed for your projects
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name