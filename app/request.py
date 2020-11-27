# from app import app
import urllib.request,json
from .main import main

# import from models
from .models import GithubUser, GithubRepositories

api_key =None
base_url = None
base_url = 'https://api.github.com/users/{}'


# def configure_request(app):
#     global api_key, base_url
#     # api_key = app.config['MOVIE_API_KEY']

#     # Getting the movie base url
#     print(app.config)
#     base_url = app.config["GITHUB_API_BASE_URl"]


# def get_github_users(username):
#     """
#     a helper function to call github api and return users
#     """
#     get_user_url = base_url.format(username)

#     print(username)

#     with urllib.request.urlopen(get_user_url) as url:
#         github_users_data = url.read()
#         github_user_response = json.loads(github_users_data)
        
#         # if get_movies_response['results']:
#         #     movie_results_list = get_movies_response['results']
#         #     movie_results = process_results(movie_results_list)

#     return username


def retrieve_github_info(user_name):
    """
    a helper function to call github api and return users
    """
    get_user_url = base_url.format(user_name)
    with urllib.request.urlopen(get_user_url) as url:
        github_users_data = url.read()
        github_user_response = json.loads(github_users_data)

        github_user = GithubUser(github_user_response['name'], github_user_response['avatar_url'], github_user_response['html_url'])

        # print('uip', github_user_response)

    return github_user


def search_github_repos():
    pass