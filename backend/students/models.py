from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    def _str_(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image_url=models.URLField(blank=True)
    stock=models.PositiveIntegerField(default=True)
    def _str_(self):
            return self.name

     