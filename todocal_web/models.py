from django.db import models


class User(models.Model):
  name = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=128)
  password = models.CharField(max_length=50)

  def __str__(self):
    return self.name
