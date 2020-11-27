import os

class Config:
    GITHUB_API_BASE_URl='https://api.github.com/users/{}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig
}