from django.shortcuts import render, render_to_response, RequestContext
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
	form = ProductForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/')

	variables = {}
	variables['form'] = form

	return render_to_response("product_form.html", variables, context_instance=RequestContext(request))