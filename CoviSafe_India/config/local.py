from decouple import config

DEBUG = True
ALLOWED_HOST = [config('PROD_HOST'),]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'covisafe_india',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

SECRET_KEY = 'django-insecure-_bgavy588xn=v69=#cn*#b#$7_et6gqp2(8v@+mjbsj)4%-yis'