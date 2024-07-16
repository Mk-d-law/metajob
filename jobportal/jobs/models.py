from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    language = models.CharField(max_length=2)
    link = models.URLField()
    pubdate = models.DateField()
    updated = models.DateField()
    salary = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    expire = models.DateField()
    jobtype = models.CharField(max_length=50)

def __str__(self):
  return self.title