from django.contrib import admin

from .models import Repository, Author

admin.site.register(Repository)
admin.site.register(Author)