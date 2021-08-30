from django.db import models
from datetime import datetime

class Quote(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete= models.SET_NULL)
    category = models.ManyToManyField(Category)
    text = models.TextField(null=True)
    published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.quote_text

    class Meta:
        ordering = ['published']

class Author(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    bio = models.TextField()
    birth_date = models.CharField(max_length=30, null=True)
    death_date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['last_name']

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
