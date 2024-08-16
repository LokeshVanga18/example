from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator , MaxValueValidator , MinValueValidator
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    std_id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    mobile_num = models.BigIntegerField(unique=True)
    address = models.TextField(blank=False)

    def __str__(self):
        return self.name

class Results(models.Model):
    std_id = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    result = models.FloatField(validators=[MinValueValidator(0.0) , MaxValueValidator(10.0)]) 

    def __str__(self):
        return f"{self.std_id.name}: {self.result}"

# class User(models.Model):
#     first_name = models.CharField(max_length=120)
#     last_name = models.CharField(max_length=210)
#     email = models.EmailField()

#     def __str__(self):
#         return self.first_name

class ClientRegister(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_url = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True , upload_to='user_details')

    def __str__(self):
        return self.user.username
