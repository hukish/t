import os
class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = ('1234')
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  
    QUOTE_API_BASE_URL = os.environ.get('QUOTE_API_BASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/nyam'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


 #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
 
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
   
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config : the parent configuration class with General configuration settings
    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}