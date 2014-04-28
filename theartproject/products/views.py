"""
product views control everything involving adding, listing, and viewing products.
"""
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.forms.formsets import formset_factory
from django.core.urlresolvers import reverse

from products.models import *
from .forms import ProductForm


"""
listProducts renders the productView template to show all the products with their images.

It also implements a filter to constrain the results it searches for.

TODO: Make filter smart, go through all the tags to filter by the tags being used.
Possible solution: Make another table with a foreign key to the product.
"""
def listProducts(request):
	allProducts = Product.objects.all()
	allImages = Image.objects.all()
	allCategories = Category.objects.all()

	if request.method == 'POST':
		answer = request.POST['value']
		#tags_list = Product.objects.filter(tags__contains=answer)
		#name_list = Product.objects.filter(name__contains=answer)
		#rtist_list = Product.objects.filter(artist__contains=answer)
		categories_list = Product.objects.filter(category__category__contains=answer)
		#allProducts = tags_list | name_list | artist_list
		allProducts = categories_list

	context = {}
	context['products'] = allProducts
	context['images'] = allImages
	context['categories'] = allCategories
	return render_to_response('productView.html', context, context_instance=RequestContext(request))

"""
addProduct adds a new product to the database

Only allows logged in admins to access the page
Saves all the information from the ProductForm into a Product object, and the images into the images table
Redirects to the list of all the products.
"""
def addProduct(request):
	if request.method == "POST":

		form = ProductForm(request.POST or None, request.FILES)

		if form.is_valid() and request.user in Group.objects.get(name="admin").user_set.all():
			save_it = form.save(commit=False)
			save_it.save()
			product = Product.objects.get(name=request.POST['name'])
			images = request.FILES
			for key, value in images.items():
				imageEntry = Image()
				imageEntry.product = product
				imageEntry.image = value
				imageEntry.save()
			for i in range(0,3):
				tag = request.POST['tag' + str(i+1)]
				if tag != "":
					tagEntry = Tag()
					tagEntry.product = product
					tagEntry.tag = tag
					tagEntry.save()
			return HttpResponseRedirect("/products/")
		else:
			return render_to_response("product_form.html", {"form":form}, context_instance=RequestContext(request))
	else:
		context = {}
		context['form'] = ProductForm()
		context['product'] = Product

		return render_to_response("product_form.html", context, context_instance=RequestContext(request))

"""
viewHomePage renders the main site's home page
"""
def viewHomePage(request):
	context = {}

	recentProducts = Product.objects.all().order_by('timestamp')
	images = []
	allImages = Image.objects.all()
	for image in allImages:
		for product in recentProducts:
			if image.product == product:
				images.append(image)

	categories = Category.objects.all()
	imageFromCategory = []
	for image in allImages:
		for category in categories:
			if image.product.category == category:
				imageFromCategory.append(image)
				break

	context['recentProducts'] = recentProducts[0:5]
	context['images'] = images
	context['categories'] = categories
	context['imageFromCategory'] = imageFromCategory
	return render_to_response('home.html', context, context_instance=RequestContext(request))
	
"""
detailProduct takes the user to the product detail's page.
It shows the product's name, artist, price, and any images.

TODO: Add the payment stuff to this page, so users can purchase products from this details page.
"""
def detailProduct(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	images = Image.objects.filter(product=product)
	return render_to_response('productDetail.html', {'product':product, 'images':images})

"""
deleteProduct takes the product completely out of the database.
"""
def deleteProduct(request, product_id):
	if request.user.is_authenticated() and request.user in Group.objects.get(name="admin").user_set.all():
		if request.method == 'POST':
			product = get_object_or_404(Product, pk=product_id).delete()
			return HttpResponseRedirect(reverse('product_list'))
	return render_to_response('productDelete.html', locals(), context_instance=RequestContext(request))

def viewProductsToDelete(request):
	if request.user.is_authenticated() and request.user in Group.objects.get(name="admin").user_set.all():
		allProducts = Product.objects.all()
		allImages = Image.objects.all()

		context = {}
		context['products'] = allProducts
		context['images'] = allImages
		return render_to_response('productsToDelete.html', context, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/")

def about(request):
	return render_to_response('about.html', locals(), context_instance=RequestContext(request))
