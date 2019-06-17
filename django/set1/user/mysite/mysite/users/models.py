from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.CharField(max_length=50)
    dob = models.DateField()    
    image = models.ImageField(upload_to='profile_pics', default='default.jpeg', null=False)

    def __str__(self):
        return f'{ self.user.username } Profile'
