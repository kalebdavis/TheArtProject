from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect

from products.models import *
from .forms import ProductForm

# Create your views here.
def listProducts(request):
	allProducts = Product.objects.all()

	variables = {}
	variables['products'] = allProducts
	return render_to_response('productView.html', variables)

def addProduct(request):
	form = ProductForm(request.POST or None, request.FILES)
	
	
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/')

	variables = {}
	variables['form'] = form
	variables['product'] = Product

	return render_to_response("product_form.html", variables, context_instance=RequestContext(request))
	
def detailProduct(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render_to_response('productDetail.html', {'product':product})