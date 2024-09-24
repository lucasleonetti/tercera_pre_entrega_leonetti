# Django App para la gestión de un sistema de prestamos de libros a clientes

## Descripción del proyecto

Este proyecto es una aplicación web desarrollada en Django que permite la gestión de un sistema de prestamos de libros a clientes. La aplicación permite registrar clientes, libros y prestamos. Asi como tambien la visualizacion de los prestamos activos y la devolucion de los libros prestados.

## Instrucciones para la ejecucion del proyecto

1.Clonar el repositorio

```bash
git clone https://github.com/lucasleonetti/tercera_pre_entrega_leonetti.git
```

2.Instalar las dependencias

```bash
pip install -r requirements.txt
```

4.Lanzar el servidor

```bash
python manage.py runserver
```

5.Acceder a la aplicación en el navegador

```bash
http://localhost:8000/book_loans/
```

### Importante

Si por algun motivo ocurre algun error o no puede visualizar los datos ya cargados en la base de datos, intente con ejecutar las migraciones nuevamente.

```bash
python manage.py migrate
```
