from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'repositories/(?P<category>\w+)/', views.show_categories, name='show_categories'),
	url(r'author/(?P<author_id>\w+)/', views.show_authors, name='show_authors'),
]