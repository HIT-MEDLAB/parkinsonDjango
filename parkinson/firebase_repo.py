import os
from pyrebase import pyrebase

config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "storageBucket": os.getenv("storageBucket")
}

firebase = pyrebase.initialize_app(config)
auth_fb = firebase.auth()
db = firebase.database()