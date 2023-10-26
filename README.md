# WebyPortal_V1
Webyops POC project Portal application that team are working with some automation features. 




# RUN AWS EC2 Server command

$ `nohup python manage.py runserver 0.0.0.0 &`

# TO RUN ON LOCAL SET THIS ALLOWED HOSTS IN SETTINGS.PY FILE
ALLOWED_HOSTS = ["ec2-13-59-151-95.us-east-2.compute.amazonaws.com", "http://ec2-13-59-151-95.us-east-2.compute.amazonaws.com:3000", "http://ec2-13-59-151-95.us-east-2.compute.amazonaws.com:3000/"]

# TO RUN ON EC2 SET THIS ALLOWED HOSTS IN SETTINGS.PY FILE
ALLOWED_HOSTS=[]

# TO ADD DJANGO DEFAULT DATABASE SET THIS IN SETTINGS.PY FILE:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        
    }
}

# TO ADD MYSQL DATABASE ON LOCAL SET THIS IN SETTINGS.PY FILE:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "webyportalv1",
        "USER": "mastersweby01",
        "PASSWORD": "WebyOps2021@mysqlmastersweby01!",
        "HOST": "ec2-13-59-151-95.us-east-2.compute.amazonaws.com",  
        "PORT": "",  
    }
}
