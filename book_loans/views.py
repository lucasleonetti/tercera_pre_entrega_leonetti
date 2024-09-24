from django.http import HttpRequest
from django.shortcuts import render

from book_loans.forms import AutorForm, ClienteForm, LibroForm, PrestamosForm
from book_loans.models import Autor, Cliente, Libro, Prestamo

# Create your views here.
def index(req: HttpRequest):
    return render(req, 'index.html')

def nuevo_libro(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_libro_form = LibroForm(req.POST)
        
        if nuevo_libro_form.is_valid():
            data = nuevo_libro_form.cleaned_data
            l = Libro(titulo=data['titulo'], autor=data['autor'], fecha_publicacion=data['fecha_publicacion'], genero=data['genero'], editorial=data['editorial'], idioma=data['idioma'], cantidad_paginas=data['cantidad_paginas'])
            l.save()
            return render(req, 'index.html')
        else:
            nuevo_libro_form = LibroForm()
            return render(req, 'nuevo_libro.html', {'nuevo_libro_form': nuevo_libro_form})
    else:
        nuevo_libro_form = LibroForm()
        return render(req, 'nuevo_libro.html', {'nuevo_libro_form': nuevo_libro_form})

def nuevo_prestamo(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_prestamo_form = PrestamosForm(req.POST)
        
        if nuevo_prestamo_form.is_valid():
            data = nuevo_prestamo_form.cleaned_data
            p = Prestamo(libro=data['libro'], fecha_prestamo=data['fecha_prestamo'], fecha_devolucion=data['fecha_devolucion'], nombre_persona=data['nombre_persona'], apellido_persona=data['apellido_persona'], dni=data['dni'], email=data['email'])
            p.save()
            return render(req, 'index.html')
        else:
            nuevo_prestamo_form = PrestamosForm()
            return render(req, 'nuevo_prestamo.html', {'nuevo_prestamo_form': nuevo_prestamo_form})
    else:
        nuevo_prestamo_form = PrestamosForm()
        return render(req, 'nuevo_prestamo.html', {'nuevo_prestamo_form': nuevo_prestamo_form})
    
def lista_prestamos(req: HttpRequest):
    prestamos = Prestamo.objects.all()
    return render(req, 'lista_de_prestamos.html', {'prestamos': prestamos})

def lista_libros(req: HttpRequest):
    libros = Libro.objects.all()
    return render(req, 'lista_de_libros.html', {'libros': libros})

def lista_clientes(req: HttpRequest):
    
    clientes = Cliente.objects.all()
    return render(req, 'lista_clientes.html', {'clientes': clientes})

def nuevo_cliente(req: HttpRequest):
    
    if req.method == 'POST':
        
        nuevo_cliente_form = ClienteForm(req.POST)
        
        if nuevo_cliente_form.is_valid():
            data = nuevo_cliente_form.cleaned_data
            c = Cliente(nombre=data['nombre'], apellido=data['apellido'], dni=data['dni'], email=data['email'])
            c.save()
            return render(req, 'index.html')
        else:
            nuevo_cliente_form = ClienteForm()
            return render(req, 'nuevo_cliente.html', {'nuevo_cliente_form': nuevo_cliente_form})
    else:
        nuevo_cliente_form = ClienteForm()
        return render(req, 'nuevo_cliente.html', {'nuevo_cliente_form': nuevo_cliente_form})
    
def lista_autores(req: HttpRequest):
    autores = Autor.objects.all()
    return render(req, 'lista_de_autores.html', {'autores': autores})

def nuevo_autor(req: HttpRequest):
        
        if req.method == 'POST':
            
            nuevo_autor_form = AutorForm(req.POST)
            
            if nuevo_autor_form.is_valid():
                data = nuevo_autor_form.cleaned_data
                a = Autor(nombre=data['nombre'], apellido=data['apellido'], fecha_nacimiento=data['fecha_nacimiento'],fecha_defuncion=data['fecha_defuncion'] ,nacionalidad=data['nacionalidad'])
                a.save()
                return render(req, 'index.html')
            else:
                nuevo_autor_form = AutorForm()
                return render(req, 'nuevo_autor.html', {'nuevo_autor_form': nuevo_autor_form})
        else:
            nuevo_autor_form = AutorForm()
            return render(req, 'nuevo_autor.html', {'nuevo_autor_form': nuevo_autor_form})
        