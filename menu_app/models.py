from django.db import models

# Create your models here.
class Appetizer(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class MainCourse(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name