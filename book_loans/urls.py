
from django.urls import path

from book_loans.views import index, lista_autores, lista_clientes, lista_libros, lista_prestamos, nuevo_autor, nuevo_cliente, nuevo_libro, nuevo_prestamo


urlpatterns = [
    path('', index),
    path('nuevo_prestamo/', nuevo_prestamo, name='nuevo_prestamo'),
    path('lista_prestamos/', lista_prestamos, name='lista_prestamos'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('lista_autores/', lista_autores, name='lista_autores'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('nuevo_autor/', nuevo_autor, name='nuevo_autor'),
    path('nuevo_cliente/', nuevo_cliente, name='nuevo_cliente'),
    path('nuevo_libro/', nuevo_libro, name='nuevo_libro'),
]
