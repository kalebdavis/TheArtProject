from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

from products.models import *
from .forms import ProductForm

# Create your views here.
def listProducts(request):
	allProducts = Product.objects.all()

	allImages = Image.objects.all()
	variables = {}
	variables['products'] = allProducts
	variables['images'] = allImages
	return render_to_response('productView.html', variables)

def addProduct(request):
	form = ProductForm(request.POST or None, request.FILES)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		product = Product.objects.get(name=request.POST['name'])
		images = request.FILES
		for key, value in images.items():
			imageEntry = Image()
			imageEntry.product = product
			imageEntry.image = value
			imageEntry.save()
		

		return HttpResponseRedirect('/products/')

	variables = {}
	variables['form'] = form
	variables['product'] = Product

	return render_to_response("product_form.html", variables, context_instance=RequestContext(request))

def viewHomePage(request):
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))
	
def detailProduct(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	images = Image.objects.filter(product=product)
	return render_to_response('productDetail.html', {'product':product, 'images':images})
