from django.db import models

# Create your models here.
class Product(models.Model):
	"""
	Defines a product for the website
	"""

	name = models.CharField(max_length=140)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	artist = models.CharField(max_length=140, null=True, blank=True)
	#image = models.ImageField(upload_to="MEDIA_ROOT/productImages")

	def __str__(self):
		return self.name