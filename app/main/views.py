from flask import render_template,request,redirect,url_for
from . import main
from ..request import retrieve_github_info

# Views
@main.route('/')
def index():
    name = "Time to get started "
    search_user = ""
    title= "search your github users"
    search_user = request.args.get('username')
    # print(search_user)
    if search_user:
            return redirect(url_for('main.get_github_users', user = search_user))
            # print(github_user_data.username)
            # title = github_user_data.username
    return render_template('index.html', name=title)

@main.route('/users/<user>')
def get_github_users(user): 
    search_user = ""
    title= "search your github users"
    search_user = request.args.get('username')
    github_user_data = retrieve_github_info(user)
    title = github_user_data.username
    return render_template('github_user.html', user=github_user_data,)
