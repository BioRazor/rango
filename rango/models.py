from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(blank=True, max_length=100, unique=True)
    views = models.SmallIntegerField(blank=True, default=0)
    likes = models.SmallIntegerField(blank=True, default=0)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, *kargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    views = models.SmallIntegerField(blank=True, default=0)


    def __str__(self):
        return self.title
