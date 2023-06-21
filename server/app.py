#!/usr/bin/env python3

from config import app, db, api, Resource, bcrypt, request

# Import models here!!!
# from models import 

# Routes!!!



if __name__ == '__main__':
    app.run( port=3000, debug=True )
