from django import forms
from .models import Product

"""
ProductForm provides the form for adding a new product.

Uses Django's ModelForm class to build the form based on the provided Product model

It also provides 4 ImageFields to give the uploader the option to upload images.
The first image is required for the new product, but the following three are optional.

TODO: Make image uploading unlimited
"""
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product

	

	tag1 = forms.CharField(max_length=140)
	tag2 = forms.CharField(max_length=140, required=False)
	tag3 = forms.CharField(max_length=140, required=False)
	tag4 = forms.CharField(max_length=140, required=False)

	image1 = forms.ImageField()
	image2 = forms.ImageField(required=False)
	image3 = forms.ImageField(required=False)
	image4 = forms.ImageField(required=False)
