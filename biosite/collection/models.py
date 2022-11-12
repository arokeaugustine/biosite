from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = ('Categories')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name

class Specimen(models.Model):
    category = models.ForeignKey(Category, related_name='Specimen', on_delete=models.CASCADE)
    common_name = models.CharField(max_length=50, blank=True)
    botanical_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='specimen_images')
    description = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,)

    class Meta:
        ordering = ('common_name',)
        verbose_name = ('Specimens')
        verbose_name_plural = ('Specimens')

    def __str__(self):
        return self.common_name