from django.contrib import admin

# Register your models here.
from .models import Students, Score

admin.site.register(Students)
admin.site.register(Score)
