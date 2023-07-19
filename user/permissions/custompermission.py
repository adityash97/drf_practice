from rest_framework.permissions import BasePermission
from user.models import MovieRatingDetail


class isAuthor(BasePermission):
    message = "Only author can edit their comment."

    def has_permission(self, request, view):
        pk = view.kwargs['pk']
        author = MovieRatingDetail.objects.get(pk=pk).user
        if request.user == author:
            return True
        return False
