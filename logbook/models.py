from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Students
# Create your models here.
class Entry(models.Model):
    weekNumber=models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    image=models.ImageField()
    studentID=models.ForeignKey(Students, on_delete=models.CASCADE)
    remarks=models.TextField()
