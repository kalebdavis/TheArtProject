from django.db import models

#you're probably lame
class Product(models.Model):
	"""
	Defines a product for the website
	"""

	name = models.CharField(max_length=140)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	artist = models.CharField(max_length=140)
	tags = models.CharField(max_length=140)

	def __str__(self):
		return self.name

#Help I'm trapped! They aren't giving me food!
class Image(models.Model):
	"""
	Images linking to product
	"""

	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='images/productthumbs')

	#I see dead people!


	#I'm reading a book about anti-gravity. I just can't put it down
