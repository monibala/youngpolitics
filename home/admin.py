from django.contrib import admin

from home.models import blog_detail, contact

# Register your models here.
admin.site.register(blog_detail)
admin.site.register(contact)