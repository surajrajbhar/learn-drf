from django.db import models

# Create your models here.
class Article(models.Model):
    authtor     =     models.CharField(max_length=100)
    title       =     models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body =        models.TextField()
    location =    models.CharField(max_length=200)
    publication = models.DateField()
    active =      models.BooleanField(default=True)
    created_at  = models.DateField(auto_now_add=True)
    updated_at =  models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.authtor} {self.title}'

