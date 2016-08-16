from django.db import models


class User(models.Model):
  name = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=128)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Schedule(models.Model):
  start_time = models.DateField()
  end_time = models.DateField()
  name = models.CharField(max_length=50)
  memo = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  repeating = models.CharField(max_length=50)

  def __str__(self):
    return self.name
    
