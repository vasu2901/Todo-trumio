from django.contrib import admin
from .models import Todo, User
# Register your models here.
admin.site.register(User)
admin.site.register(Todo)