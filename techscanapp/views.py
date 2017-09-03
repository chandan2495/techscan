from django.shortcuts import render
from django.http import HttpResponse
from techscanapp.models import Repository, Author
import requests

def index(request):
	'''show categoies (javascript , java, python, php, ruby)'''
	categoies = ['JavaScript', 'Java', 'Python', 'Php', 'Ruby']
	context = dict()
	context["data"] = []
	for cat in categoies:
		repos = Repository.objects.filter(language=cat)
		new_repo = {}
		new_repo['language'] = cat
		new_repo['count'] = len(repos)
		context["data"].append(new_repo)	
	return render(request, 'techscan/index.html', context)

def show_categories(request, category):
	'''show repositories for selected category'''
	def compare_popular(a):
		return a.stargazers_count
	context = dict()
	context["data"] = []
	repos = Repository.objects.filter(language=category)
	repos = sorted(repos, key=compare_popular, reverse = True)
	context["data"] = context['data'] + list(repos)
	return render(request, 'techscan/show_category.html', context)

def show_authors(request, author_id):
	'''show author profile'''
	def compare_popular(a):				
		return a["stargazers_count"]
	context = dict()
	context["data"] = {}
	author_profile = Author.objects.get(pk=author_id)
	print(author_profile.repos_url)
	repos = requests.get(author_profile.repos_url)
	repos = repos.json()
	context["data"]["author_profile"] = author_profile
	repos1 = sorted(repos, key=compare_popular, reverse = True)
	context["data"]["repos"] = repos1

	return render(request, 'techscan/show_author_profile.html', context)
