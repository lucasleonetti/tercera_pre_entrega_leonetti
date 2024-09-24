from django import forms

from book_loans.models import Autor, Cliente, Libro, Prestamo


class PrestamosForm(forms.Form):
    class Meta:
        model = Prestamo
        fields = ['libro', 'fecha_prestamo', 'fecha_devolucion', 'nombre_persona', 'apellido_persona', 'dni', 'email']
    
    
    libro = forms.ModelChoiceField(
        queryset = Libro.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-4'}),
        label='Seleccione el libro'
    )

    fecha_prestamo = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Ingrese la fecha de préstamo', 'class': 'form-control mb-4', 'type': 'date'}),
        label='Fecha de préstamo'
    )

    fecha_devolucion = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'Ingrese la fecha de devolución', 'class': 'form-control mb-4', 'type': 'date'}),
        label='Fecha de devolución'
    )

    nombre_persona = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre de cliente', 'class': 'form-control mb-4'}),
        label='Nombre de cliente'
    )

    apellido_persona = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido de cliente', 'class': 'form-control mb-4'}),
        label='Apellido de cliente'
    )

    dni = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Ingrese DNI de cliente', 'class': 'form-control mb-4'}),
        label='DNI de cliente'
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Ingrese email de cliente', 'class': 'form-control mb-4'}),
        label='Email de cliente'
    )
    
    
class ClienteForm(forms.Form):
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'email']
    
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre de cliente', 'class': 'form-control mb-4' }), label='Nombre de cliente')
    
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido de cliente', 'class': 'form-control mb-4' }), label='Apellido de cliente')
    
    dni = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ingrese DNI de cliente', 'class': 'form-control mb-4' }), label='DNI de cliente')
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingrese email de cliente', 'class': 'form-control mb-4' }), label='Email de cliente')


class LibroForm(forms.Form):
    
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'genero', 'editorial', 'idioma', 'cantidad_paginas']
        
    titulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese título de libro', 'class': 'form-control mb-4' }), label='Título de libro')
    
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), widget=forms.Select(attrs={'class': 'form-control mb-4'}), label='Seleccione el autor', required=True, empty_label='Seleccione el autor')
    
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Ingrese fecha de publicación', 'class': 'form-control mb-4', 'type': 'date'}), label='Fecha de publicación')
    
    genero = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese género de libro', 'class': 'form-control mb-4' }), label='Género de libro')
    
    editorial = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese editorial de libro', 'class': 'form-control mb-4' }), label='Editorial de libro')
    
    idioma = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese idioma de libro', 'class': 'form-control mb-4' }), label='Idioma de libro')
    
    cantidad_paginas = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ingrese cantidad de páginas de libro', 'class': 'form-control mb-4' }), label='Cantidad de páginas de libro')
    
    
class AutorForm(forms.Form):
    
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'fecha_defuncion', 'nacionalidad']
    
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre de autor', 'class': 'form-control mb-4' }), label='Nombre de autor')
    
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido de autor', 'class': 'form-control mb-4' }), label='Apellido de autor')
    
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Ingrese fecha de nacimiento de autor', 'class': 'form-control mb-4', 'type': 'date' }), label='Fecha de nacimiento de autor')
    
    fecha_defuncion = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Ingrese fecha de defunción de autor', 'class': 'form-control mb-4', 'type': 'date' }), label='Fecha de defunción de autor', required=False)
    
    nacionalidad = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ingrese nacionalidad de autor', 'class': 'form-control mb-4' }), label='Nacionalidad de autor')