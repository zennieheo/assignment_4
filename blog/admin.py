from django.contrib import admin
from .models import Blog
# models 라는 파일을 통해 Blog을 import 해온 거임


admin.site.register(Blog)

# Register your models here.
