# from app import app
import urllib.request,json
from .main import main

# import from models
from .models import GithubUser, GithubRepositories

api_key =None
base_url = None
base_url = 'https://api.github.com/users/{}'


def retrieve_github_info(user_name):
    """
    a helper function to call github api and return users
    """
    get_user_url = base_url.format(user_name)
    with urllib.request.urlopen(get_user_url) as url:
        github_users_data = url.read()
        github_user_response = json.loads(github_users_data)

        print(type(github_user_response))

        github_user = GithubUser(github_user_response['name'], github_user_response['avatar_url'], github_user_response['html_url'])
        # github_user = GithubUser(github_user_response.get('namee'), github_user_response['avatar_url'], github_user_response['html_url'])

        # print('uip', github_user_response)

    return github_user


def search_github_repos():
    pass