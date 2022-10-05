from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from PIL import Image
import os
from django.conf import settings


class Product(models.Model):
    prod_name = models.CharField(
        default='', max_length=50, verbose_name='Name')
    prod_description_short = models.CharField(
        max_length=100, verbose_name='Short description')
    prod_description_long = models.CharField(
        max_length=1000, verbose_name='Long description')
    prod_image = models.ImageField(
        upload_to='product_image/%Y/%m',
        blank=True, null=True, verbose_name='Image')
    prod_slug = models.SlugField(unique=True, verbose_name='Slug')
    prod_price = models.FloatField(verbose_name='Price')
    prod_price_sale = models.FloatField(default=0, verbose_name='Sale price')
    prod_type = models.CharField(
        default='V', max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        ),
        verbose_name='Product type',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 800
        if self.prod_image:
            self.resize_image(self.prod_image, max_image_size)

    @staticmethod
    def resize_image(image, new_width=800):
        img_path = os.path.join(settings.MEDIA_ROOT, image.name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            img.close()
            return

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(img_path, optimize=True, quality=70)
        new_img.close()

    def __str__(self):
        return self.prod_name


class Variety(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Product')
    variety_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Name')
    variety_price = models.FloatField(verbose_name='Price')
    variety_price_sale = models.FloatField(
        default=0, verbose_name='Sale price')
    variety_inventory = models.PositiveIntegerField(
        default=0, verbose_name='Inventory')

    def __str__(self):
        return self.variety_name or self.product

    class Meta:
        verbose_name = 'Variety'
        verbose_name_plural = 'Varieties'
