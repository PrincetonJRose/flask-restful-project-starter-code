#!/usr/bin/env python3

from random import randint, choice as rc
from faker import Faker
from app import app

# Don't forget to import models here too!!!
# from models import 

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Seeding... 🌱")


        print( 'Wiping tables...' )
        # Clear all the tables!

        print( 'Database wiped!' )


        print( 'Creating ______ ...' )

        print( '_________ created!' )
