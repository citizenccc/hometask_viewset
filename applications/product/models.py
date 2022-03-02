from django.db import models

from applications.product.utils import slug_generator


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True,
                            blank=True)
    price = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title