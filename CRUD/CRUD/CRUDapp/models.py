from django.db import models

# Create your models here.
class Student_Entry(models.Model):
    roll_no = models.PositiveIntegerField(unique=True, null=True)
    fname = models.TextField(max_length=50)
    lname = models.TextField(max_length=50)
    s_class = models.TextField(max_length=50)
    subject = models.CharField(max_length=50)
    marks = models.PositiveIntegerField()
    
    def __str__(self):
        return self.roll_no

    class Meta:
        # verbose_name = "Student Entry"
        verbose_name_plural = "Student Entry" # it will change Admin site Table Name
