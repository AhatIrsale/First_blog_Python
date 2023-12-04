from django.contrib import admin
from .models import *
for model in [Bloguer, Blog]:
    admin.site.register(model)

# Register your models here.
