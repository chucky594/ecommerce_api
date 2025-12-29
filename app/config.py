import os         
from datetime import timedelta    
from dotenv import load_dotenv

load_dotenv()

class Config():
    '''
    Application configuration settings
    settings specific for different environments
    '''
    
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_ECHO= False
    
    JWT_SECRET_KEY= os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES= timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES= timedelta(days=30) 
    
    ITEMS_PER_PAGE= 20
    
    CORS_ORIGINS= os.environ.get('CORS_ORIGINS', '*').split(',')
    
    
    
class DevelopmentConfig(Config):
    
    '''
    Development Environment Configuration
    
    -Debug is enabled
    - SQLite database is found in instance folder 
    '''
    
    DEBUG = True
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_ECHO = True
    
class TestingConfig(Config):
    '''
    Testing enivronment configuration 
    -Testing is enabled
    -CSRF is disabled for easier testing 
    -In-memory database is fast
    '''
    
    DEBUG = False
    TESTING = True
    
    SQLALCHEMY_DATABASE_URI = 'splite:///:memory'
    
    WTF_CSRF_ENABLED = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    
    
class ProductionConfig(Config):
    '''
    Docstring for ProductionConfig
    '''
    DEBUG = True
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    if not os.environ.get('SECRET_KEY'):
        raise ValueError('SECRET_KEY environment must be set in production')
    
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    CORS_ORIGINS= os.environ.get('CORS_ORIGINS', '*').split(',')
    if not CORS_ORIGINS or CORS_ORIGINS == ['']:
        raise ValueError('CORS_ORIGINS must be set in production')
    
    
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
        