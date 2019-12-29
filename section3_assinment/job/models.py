from django.db import models

# Create your models here.

class joboffer(models.Model):
    company_name  =  models.CharField(max_length=100)
    company_email =  models.EmailField(max_length=500)
    job_title = models.CharField(max_length=100)
    job_description  = models.TextField()
    salary =  models.FloatField()
    city = models.CharField(max_length=100)
    state =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    available =  models.BooleanField(default=True)

    class Meta:
        def __str__(self):
            return self.company_email


    
    