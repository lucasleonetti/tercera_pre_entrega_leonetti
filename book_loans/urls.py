
from django.urls import path

from book_loans.views import index, lista_clientes, lista_libros, lista_prestamos, nuevo_prestamo


urlpatterns = [
    path('', index),
    path('nuevo_prestamo/', nuevo_prestamo, name='nuevo_prestamo'),
    path('lista_prestamos/', lista_prestamos, name='lista_prestamos'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
]
