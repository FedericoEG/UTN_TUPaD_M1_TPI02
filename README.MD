# Trabajo Práctico Integrador 2
### Materia: Matemática
### Alumnos: Federico Esteban Garcia y Federico Garcia Bengolea
#### Cátedra 14

## Docentes
### Profesor/a: Vanina Durrutty
### Tutor/a: Ana Maria Castro

## Descripción
Este repositorio contiene los archivos necesarios para utilizar una aplicación que satisface las secciones A y B de la parte 2  del trabajo práctico integrador.
Lo relacionado a la parte 1, se puede encontrar en un archivo de este mismo repositorio en formato PDF llamado `MTM - TP INTEGRADOR [Conjuntos y Logica].pdf`.
La parte 3 es el video de presentación del proyecto que lo pueden ver [acá](https://www.youtube.com/watch?v=AH3lsngIwcw).

[![Alt text](https://img.youtube.com/vi/AH3lsngIwcw/0.jpg)](https://www.youtube.com/watch?v=AH3lsngIwcw)

#### La aplicación permite:
Dar de alta conjuntos utilizando como fuente un DNI o un año. Una vez creados los conjuntos la aplicación despliega un menú del cual se pueden elegir diversas opciones para realizar operaciones con los conjuntos que se encuentran en memoria.

## Utilización
Para poder utilizar el programa es necesario tener instalada la dependencia `COLORAMA`. Ésta puede ser instalada mediante el compando `pip install colorama` o bien utilizando el archivo `requirements.txt` que se encuentra en el repositorio. Para realizar la instalación mediante el archivo de requerimientos se puede utilizar el comando `pip install -r requirements.txt`.

Una vez instalada la dependecia necesaria se puede proceder a ejecutar el programa corriendo el comendo `python main.py`. Esto desplegará un menu con el cual el usuario podrá interactuar y ejecutar todas las funciones detalladas en la descripción.

Los códigos de las operaciones a realizar pueden ser ingresados tanto en mayúsculas como en minúsculas a pesar de que el menú muestra las opciones en mayúsuculas. La opción para salir del programa es **SP - salir del programa**.

>La aplicación cuenta con un seeder que automáticamente agrega conjuntos. Estos conjuntos pueden ser eliminados como cualquier otro conjunto, pero cada vez que se inicia la aplicación se van a volver a crear. Es útil para hacer pruebas sin la necesidad de ingresar nuevos conjuntos cada vez que uno incia el programa.

