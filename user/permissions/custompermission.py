from rest_framework.permissions import BasePermission
from user.models import MovieRatingDetail
from rest_framework import permissions

class isAuthor(BasePermission):
    message = "Only author can edit their comment."

    def has_permission(self, request, view):
        pk = view.kwargs['pk']
        author = MovieRatingDetail.objects.get(pk=pk).user
        if request.user == author:
            return True
        return False
    
    
class IsAuth_Or_ReadOnly(BasePermission):
    
    def has_permission(self,request,view): # Overriding from base permission
        if request.user:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        
        
        return False
