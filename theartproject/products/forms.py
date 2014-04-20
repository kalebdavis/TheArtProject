from django import forms


from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product

	image1 = forms.ImageField()
	image2 = forms.ImageField(required=False)
	image3 = forms.ImageField(required=False)
	image4 = forms.ImageField(required=False)
