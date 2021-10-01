SECRET_KEY = 'django-insecure-sa8u_o+$%2ct37g%lr(e9gf1n9tl_r6zy!da&z!+qu5n95922i'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'stammer91',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit' : True
        }
    }
}