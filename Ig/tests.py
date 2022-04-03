from django.test import TestCase
from .models import Comments, Image, Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='Softdev')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="mypic.png")
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_user_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
