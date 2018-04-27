from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.URLField(max_length=1000)


    def __str__(self):
        return self.name
