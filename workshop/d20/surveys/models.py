from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    votes = models.IntegerField()