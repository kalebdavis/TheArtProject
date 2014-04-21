from django.contrib import admin
from adminuser.models import Admin

"""
If the superuser wants to be able to see models on the built-in Django site, register them
to the admin site on this page. Make sure to import the model above first.
"""

admin.site.register(Admin)