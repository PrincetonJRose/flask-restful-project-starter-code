#!/usr/bin/env python3

# Local imports
from config import app, db, api, Resource, bcrypt, request

# Import models here!!!
# from models import 

# Routes!!!

if __name__ == '__main__':
    app.run( port=5555, debug=True )
