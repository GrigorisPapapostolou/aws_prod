from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.
def get_upload_file_name(profile, filename):
    return 'images/%s/%s_%s' %  (str(profile.user.username), str(datetime.now().strftime("%d_%m_%Y_%H:%M:%S")).replace(':', '_'), filename)


class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='Default.png', upload_to=get_upload_file_name)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
