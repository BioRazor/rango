from django.db import models

class Category(models.Model):
    name = models.CharField(blank=True, max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    Category = models.ForeignKey(Category)
    tittle = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    views = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return self.tittle
