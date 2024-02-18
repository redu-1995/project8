from django.db import models


class BookInformation(models.Model):
   name  = models.CharField(max_length=100)
   description = models.TextField()
   
   def __str__(self) -> str:
      return self.name
   
class Category(models.Model):
   name  = models.CharField(max_length=100)
   

   def __str__(self) -> str:
      return self.name
   
   
class Book(models.Model):
   Book_name = models.CharField(max_length=100)
   Book_description = models.TextField()   
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   image  = models.ImageField(null=True)
   price   = models.FloatField(null=True)
   date   = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self) -> str:
      return self.Book_name
   
