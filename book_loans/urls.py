
from django.urls import path

from book_loans.views import index


urlpatterns = [
    path('', index)
]
