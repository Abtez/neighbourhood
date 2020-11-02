from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from phone_field import PhoneField
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
import uuid

class Neighbourhood(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    population = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_name')
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def find_neighbourhood(self, pk):
        place = get_object_or_404(Neighbourhood, id=pk)
        return Neighbourhood.objects.filter(location=place)
    
    @classmethod
    def update_neighbourhood(cls, id, value):
        cls.objects.filter(id=id).update(population=value)
        
    @classmethod
    def update_count(cls, id, value):
        cls.objects.filter(id=id).update(population=value).count()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=120, null=True)
    avatar = CloudinaryField('image')
    city = models.CharField(max_length=150, null=True)
    Country = models.CharField(max_length=150, null=True)
    # neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Business(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='business_user')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def find_business(self, pk):
        work = get_object_or_404(Business, id=pk)
        return Business.objects.filter(name=work)
   
    @classmethod
    def update_business(cls, id, value):
        cls.objects.filter(id=id).update(name=value)
        
    @classmethod
    def search_business(cls,search_term):
        job = Business.objects.filter(name__icontains=search_term)
        return job
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = CloudinaryField('image')
    title = models.CharField(max_length=120, null=True)
    content = models.TextField(max_length=1000, verbose_name='project Description', null=True)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_profile')
    
    def __str__(self):
        return self.title