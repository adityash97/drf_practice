from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.



# class User(User):
#     # fname = models.CharField(max_length=250)
#     # lname = models.CharField(max_length=250)
#     # mobile = models.CharField(blank=True,null=True,max_length=100)
#     # email = models.EmailField(blank=True,null=True)
#     dob = models.DateField(blank=True,null=True)
#     age = models.IntegerField(blank=True,null=True)
#     prefered_genre = models.ManyToManyField('movielist_app.Genre',blank=True)
#     created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    
#     def __str__(self):
#         return self.fname + self.lname

class MovieRatingDetail(models.Model):
    movie = models.ForeignKey('movielist_app.Movie',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5)],default=0)
    like = models.BooleanField(default=False) # TODO : user might like it(True) or donot like(False) or do nothing (Null)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    
class Token(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.token
    