from django.db import models

class Repository(models.Model):	    
    repository_id = models.IntegerField(default=0,null=True)
    name = models.CharField(max_length=1024,null=True)
    full_name = models.CharField(max_length=1024,null=True)
    html_url = models.CharField(max_length=1024,null=True)
    description = models.CharField(max_length=20000,null=True)
    stargazers_count = models.IntegerField(default=0,null=True)
    language = models.CharField(max_length=1024,null=True)
    forks_count = models.IntegerField(default=0,null=True)
    watchers = models.IntegerField(default=0,null=True)
    # this will be from the Author table 
    author_id = models.IntegerField(default=0,null=True)

class Author(models.Model):
	user_id = models.IntegerField(default=0,null=True)
	login = models.CharField(max_length=1024,null=True)
	avatar_url = models.CharField(max_length=1024,null=True)
	html_url = models.CharField(max_length=1024,null=True)
	repos_url = models.CharField(max_length=1024,null=True)
	followers_url = models.CharField(max_length=1024,null=True)
	following_url = models.CharField(max_length=1024,null=True)