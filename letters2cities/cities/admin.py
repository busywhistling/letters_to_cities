from django.contrib import admin

# Register your models here.
from .models import City, Letter
admin.site.register(City)
admin.site.register(Letter)