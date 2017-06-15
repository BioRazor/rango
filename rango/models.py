from django.db import models

class Category(models.Model):
    name = models.CharField(blank=True, max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def _str__(self):
        pass
