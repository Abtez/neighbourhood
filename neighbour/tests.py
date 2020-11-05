from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from .models import *
import datetime as dt

class ProfileTestCase(TestCase):
    def setUp(self):
        hood_name = Name(neighbourhood_name='CBD')
        user = User.objects.create_user(username='testusereres', password='12345')
        neighbourhood = Neighbourhood(hood_name=hood_name, location='Nai', population=10, admin=user)
        
        self.profile = Profile(user=user, bio='me..me', avatar='image.jpg', neighbourhood=neighbourhood)
                
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
class NameTestCase(TestCase):
    def setUp(self):
        self.hood = Name(neighbourhood_name='CBD')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Name))
        
class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testusereres', password='12345')
        hood_name = Name(neighbourhood_name='CBD')
        self.neighbour = Neighbourhood(hood_name=hood_name, location='Nai', population=10, admin=user)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbour, Neighbourhood))
        
class BusinessTestCase(TestCase):
    def setUp(self):
        hood_name = Name(neighbourhood_name='CBD')
        user = User.objects.create_user(username='testusereres', password='12345')
        neighbourhood = Neighbourhood(hood_name=hood_name, location='Nai', population=10, admin=user)
        profile = Profile(user=user, bio='me..me', avatar='image.jpg', neighbourhood=neighbourhood)
        self.business = Business(name='DevOps', description='coding', user=profile,neighbourhood=neighbourhood)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))
        
    
