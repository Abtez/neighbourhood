from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from .models import *
import datetime as dt

class ProfileTestCase(TestCase):
    def setUp(self):
        hood_name = Name(neighbourhood_name='CBD')
        user = User.objects.create_user(username='testusereres', password='12345')
        neighbourhood = Neighbourhood(hood_name=hood_name, location='Nai', populatio=10, admin=user)
        
        self.profile = Profile(user=user, bio='me..me', avatar='image.jpg', neighbourhood=neighbourhood)
                
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    
