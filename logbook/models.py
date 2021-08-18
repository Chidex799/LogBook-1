from django.db import models
from accounts.models import Students
# Create your models here.
class Entry(models.Model):
    weekNumber=models.IntegerField(blank = False, null = False)
    dateTime = models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank = False, null = False)
    image=models.URLField(blank = True, null= True)
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    remarks=models.TextField(blank = True, null = True)

