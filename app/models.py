
class GithubUser:
    def __init__(self, username, avatar_url, url):
        self.username = username
        self.avatar_url = avatar_url
        self.url = url


class GithubRepositories:
    
    def __init__(self, repo):
        self.repo = repo