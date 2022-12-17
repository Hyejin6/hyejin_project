from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post) # 어드민에서 post관리할 수 있게 등록
