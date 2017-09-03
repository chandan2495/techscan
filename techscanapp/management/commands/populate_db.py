from django.core.management.base import BaseCommand
from techscanapp.models import Repository, Author
import json
import requests


class Command(BaseCommand):
    args = ''
    help = 'populating db from techscan.json file'

    def loadLocalJsonDump(self, path):
        data = []
        with open(path) as techscan:
            for line in techscan:
                data.append(json.loads(line))
        return data

    def getRepoData(self, repo_url):
        repo = requests.get(repo_url)
        if repo.status_code == 200:
            data = repo.json()
            return True,data
        return False,""

    def storeAndGetAuthor(self, owner):
        print('Saving author details %d ' % owner['id'])
        user_id = owner['id']
        login = owner['login']
        avatar_url = owner['avatar_url']
        html_url = owner['html_url']
        repos_url = owner['repos_url']
        followers_url = owner['followers_url']
        following_url = owner['following_url']
        try:
            author = Author.objects.get(user_id=int(user_id))
            print('Already Exists author %d ' % owner['id'])
        except:
            author = Author(user_id=user_id, login=login, avatar_url=avatar_url, html_url=html_url,
                            repos_url=repos_url, followers_url=followers_url, following_url=following_url)
            author.save()        
        return author.id

    def storeRepository(self, repo, author_id):
        print('Saving repository %d ' % repo['id'])
        repository_id = repo['id']
        name = repo['name']
        full_name = repo['full_name']
        html_url = repo['html_url']
        description = repo['description']
        stargazers_count = repo['stargazers_count']
        language = repo['language']
        forks_count = repo['forks_count']
        watchers = repo['watchers']
        # this will be from the Author table
        author_id = author_id
        try:
            Repository.objects.get(repository_id=repository_id)
            print('Already Exists repository %d ' % repo['id'])
        except:
            repository = Repository(repository_id=repository_id, name=name, full_name=full_name, html_url=html_url, description=description,
                                    stargazers_count=stargazers_count, language=language, forks_count=forks_count, watchers=watchers, author_id=author_id)
            repository.save()

    def storeInDatabase(self, data):
        repo_url = data['repo']['url']
        print(repo_url)
        status, repo = self.getRepoData(repo_url)   
        print(status) 
        if status:    
	        author_id = self.storeAndGetAuthor(repo['owner'])
	        self.storeRepository(repo, author_id)

    def handle(self, *args, **options):
        path = 'techscanapp/techscan.json'
        print(path)
        jsonData = self.loadLocalJsonDump(path)
        print(len(jsonData))
        for data in jsonData:
            self.storeInDatabase(data)
