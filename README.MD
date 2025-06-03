# Trabajo Práctico Integrador 2
### Materia: Matemática
### Alumnos: Federico Esteban Garcia y Federico Garcia Bengolea

## Docentes
### Profesor/a: Vanina Durrutty
### Tutor/a: Ana Maria Castro

## Descripción
Este repositorio contiene los archivos necesarios para utilizar una aplicación que satisface la sección A de la segunda parte del trabajo práctico integrador.
#### La aplicación permite:
* Creación de conjuntos utilizando como elelemntos del mismo los valores de un DNI
* Viasualizar el total de conjuntos cargados en la memoria
* Eliminar un conjunto de la lista
* Viasualizar la unión de dos de estos conjuntos a elección
* Visualizar la intersección de dos de estos conjuntos a elección
* Visualizar la diferencia de dos de estos conjuntos a elección
* Visualizar la diferencia simétrica de dos de estos conjuntos a elección
* Realizar la sumatorio de los dígitos del DNI con el que se generó el conjunto
* Realizar el conteo de apariciones de cada dígito en el DNI con el que se generó el conjunto
* Realizar un análisi de todos los elementos de los conjuntos que se encuentran en memoria en ese momento

## Utilización
Para poder utilizar el programa es necesario tener instalada la dependencia `COLORAMA`. Ésta puede ser instalada mediante el compando `pip install colorama` o bien utilizando el archivo `requirements.txt` que se encuentra en el repositorio. Para realizar la instalación mediante el archivo de requerimientos se puede utilizar el comando `pip install -r requirements.txt`.

Una vez instalada la dependecia necesaria se puede proceder a ejecutar el programa corriendo el comendo `python main.py`. Esto desplegará un menu con el cual el usuario podrá interactuar y ejecutar todas las funciones detalladas en la descripción.

Los códigos de las operaciones a realizar pueden ser ingresados tanto en mayúsculas como en minúsculas a pesar de que el menú muestra las opciones en mayúsuculas. La opción para salir del programa es **SP - salir del programa**.

>La aplicación cuenta con un seeder que automáticamente agrega 3 conjuntos con sus respectivos DNI. Estos conjuntos pueden ser eliminados como cualquier otro conjunto, pero cada vez que se inicia la aplicación se van a volver a crear. Es útil para hacer pruebas sin la necesidad de ingresar nuevos conjuntos cada vez que uno incia el programa.

