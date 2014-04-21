from django.db import models

"""
Product class is any piece of artwork that will be uploaded to the store

It has a name, price, artist, and tags. All of these fields are required.
"""
class Product(models.Model):
	name = models.CharField(max_length=140)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	artist = models.CharField(max_length=140)
	tags = models.CharField(max_length=140)

	def __str__(self):
		return self.name

"""
Image class provides a table to hold the different images uploaded for each product

Holds a ForeignKey to the Product as well as the path to the Image

This allows for as many images as are wanted to apply to one Product.
"""
class Image(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='images/productthumbs')