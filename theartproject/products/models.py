from django.db import models

# Create your models here.
class Product(models.Model):
	"""
	Defines a product for the website
	"""

	name = models.CharField(max_length=140)
	price = models.DecimalField(max_digits=5,decimal_places=2)
<<<<<<< HEAD
	artist = models.CharField(max_length=140, null=True, blank=True)
	#image = models.ImageField(upload_to="MEDIA_ROOT/productImages")
=======
	artist = models.CharField(max_length=140)
	tags = models.CharField(max_length=140)
	image = models.FileField(upload_to='images/%Y/%m/%d')
>>>>>>> 8e4087af54da8259cd6194d6074ed189090c3924

	def __str__(self):
		return self.name