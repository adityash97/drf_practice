from django.contrib import admin
from .models import User
<<<<<<< HEAD
from .models import Token
# Register your models here.

admin.site.register(User)
admin.site.register(Token)
=======
from .models import Token 
from .models import MovieRatingDetail
# Register your models here.

admin.site.register(User)
admin.site.register(Token)
admin.site.register(MovieRatingDetail)
>>>>>>> 012a879 (https://github.com/adityash97/drf_practice/issues/1 : CRUD complete)
