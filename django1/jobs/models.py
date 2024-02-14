from django.db import models

# Create your models here.

class jobHiring(models.Model):
    jobTitle = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    salary = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.jobTitle} - {self.address} - ${self.salary}"