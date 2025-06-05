from colorama import Fore, Back, Style
from itertools import product
from datetime import datetime

from os import system as os_system

from platform import system as pl_system

from constants import OPTIONS

#Es una función seeder porque me cansé de ingresar siempre data para poder probar.
def seed():
  seeded_sets = {}
  seeded_sets["A"] = {"DNI": [3, 0, 6, 1, 1, 0, 9, 2], "SET": ["0", "1", "2", "3", "6", "9"]}
  seeded_sets["B"] = {"DNI": [9, 4, 9, 6, 6, 9, 5, 5], "SET": ["4", "5", "6", "9"]}
  seeded_sets["C"] = {"DNI": [1, 1, 6, 7, 7, 8, 6, 7], "SET": ["1","6","7","8"]}
  seeded_sets["D"] = {"AÑO": [2, 0, 1, 7], "SET": ["0", "1", "2", "7"]}
  seeded_sets["E"] = {"AÑO": [1, 9, 9, 5], "SET": ["1","5","9"]}
  seeded_sets["F"] = {"AÑO": [1, 9, 9, 5], "SET": ["1","5","9"]}
  seeded_sets["G"] = {"AÑO": [2, 0, 2, 4], "SET": ["0","2","4"]}
  return seeded_sets

#Esta función se encarga de devolver los elementos únicos de un array.
def sorted_unique_elements(elements):
  elements_without_char = []
  for element in elements:
    if element.isdigit():
      elements_without_char.append(element)
  unique_element_list = list(set(elements_without_char))
  unique_element_list.sort()
  return unique_element_list

#Esta función se encarga de mostrar el mensaje de input y devuelve su valor capitalizado.
def upper_input(message):
	return input (message).upper()

#Esta función ordena los elementos de un array y los devuelve separados por comas como un string.
def join_and_sort(elements):
  elements.sort()
  return ",".join(elements)

def build_num(elements):
  return ''.join(map(str, elements))

#Esta función transforma el valor string a un array de numeros.
def num_to_array(num):
  array = []
  for char in num:
    if char.isdigit():
      array.append(int(char))
  return array

#Esta función detecta el sistema operativo en el que se está corriendo el programa y ejecuta la función apropiada para borrar la consola.
def clear_console():
    if pl_system() == "Windows":
        os_system('cls')
    else:
        os_system('clear')

#Esta función genera un separador para la consola.
def separator(character = "-", qty = 60):
  separator = character * qty
  print(Fore.LIGHTMAGENTA_EX + f"{separator}" + Fore.RESET)

#Esta función es para lanzar un mensaje de error en la consola.
def error(message):
  clear_console()
  print(Fore.RED + message + Style.RESET_ALL)

#Esta funcion se encarga de imprimer el mensaje de bienvenida, incluyendo una descripción de la aplicación y un listado detalladod e las operaciones posibles.
def show_welcome():
  clear_console()
  print(Fore.GREEN + f"======================= Bienvenido =======================")
  print(Fore.GREEN + f"Esta es una aplicación creada por alumnos de la comisión\n14 de la Tecnicatura Universitaria en programación\ndictada por la UTN. Corresponde al trabajo integrador de\nla materia MATEMÁTICA I. En esta se podrán ingresar\nnúmeros de documento y años de nacimiento para que sean\nconvertidos a conjuntos y poder operar con los mismos.")
  print()
  print(Fore.MAGENTA + f"Las operaciones definidas son:")
  print(Fore.MAGENTA + f"* Unión => 'U'")
  print(Fore.MAGENTA + f"* Intersección => 'I'")
  print(Fore.MAGENTA + f"* Diferencia => 'D'")
  print(Fore.MAGENTA + f"* Disferencia Simétrica => 'DS'")
  print(Fore.RESET)

#Esta función se encarga de mostrar las selecciones posibles y de comprobar que la selección realizada sea válida. Ya sea por recibir una opción no listada o que la cantidad de conjuntos no sea la correcta para la ejecución de la operación solicitada.
def options_menu(number_of_sets):
    option = None
    separator()
    print()
    print(Fore.BLACK + Back.CYAN + f" -> Actualmente tienes {number_of_sets} conjuntos ingresados <- " + Style.RESET_ALL)
    print()
    print("Que operación quieres realizar?")
    for key, option in OPTIONS.items():
      print(f"* '{key}' para {option['description']}")
    option = input("Ingresa la opción que quieras realizar: ").upper()
    while (option not in OPTIONS.keys()) or (OPTIONS[option]["sets_required"] > number_of_sets):
      print(Fore.RED + "Esa opción es incorrecta, por favor revisa tu selección y controla que tengas la cantidad de conjuntos necesaria para poder seleccionarla")
      option = input(Fore.RESET + "Ingresa la opción que quieras realizar: ").upper()
    print(Fore.RESET)
    return option

#Esta función ingresa un nuevo conjunto al listado de conjuntos. Ya se encarga de normalizar los elementos ingresados para que sean únicos.
def insert_set(actual_sets, number_of_sets, key):
  if key == 1:
     key_name = "DNI"
  else:
     key_name = "AÑO DE NACIMIENTO"
  separator()
  overrite = "no"
  set_name = input("Ingrese el nombre deseado para su conjunto. Se recomienda utilizar una letra MAYUSCULA: ")
  while set_name in list(actual_sets.keys()) and overrite == "no":
    overrite = input(Back.LIGHTYELLOW_EX + "El nombre seleccionado ya está en uso. Desea sobreescribir el conjunto? (si/no): " + Style.RESET_ALL)
    if overrite == "no":
      set_name = input("Ingrese el nombre deseado para su conjunto. Se recomienda utilizar una letra MAYUSCULA: ")
    else:
      overrite = "si"
  set_values = input(f"Ingrese su número de {key_name} sin carácteres de por medio para ser convertido en los valores del conjunto: ")
  actual_sets[set_name.upper()] = {}
  if key == 1:
    actual_sets[set_name]["DNI"] = num_to_array(set_values)
    actual_sets[set_name]["SET"] = sorted_unique_elements(list(set_values))
  else:
    actual_sets[set_name]["AÑO"] = num_to_array(set_values)
    actual_sets[set_name]["SET"] = sorted_unique_elements(list(set_values))
  number_of_sets = len(actual_sets.keys())
  clear_console()
  separator()
  print(Back.LIGHTGREEN_EX + Fore.GREEN + f"El conjunto fue agregado exitosamente!" + Style.RESET_ALL)
  print()
  show_sets(actual_sets, False)
  return number_of_sets

#Esta función imprime los conjuntos que se le pasen por parámetro.
def show_sets(actual_sets, clear_before = True):
  if clear_before:
    clear_console()
    separator()
  print("Los conjuntos actualmente cargados son:", "\n")
  for key, elements in actual_sets.items():
    set_representation = join_and_sort(elements["SET"])
    main_key = next(iter(elements.keys() - {"SET"}), "Error al obtener dato: key") 
    print(Fore.YELLOW + f"{key}=" + Fore.BLACK + Back.YELLOW + f"{{{set_representation}}} creado con el {main_key}: {build_num(elements[main_key])}" + Style.RESET_ALL)
    print()

# Determina si un año es bisiesto
def is_leap_year(year):
  return True if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else False

# Cuenta la cantidad de años pares e impares hay en los conjuntos con key="AÑO"
def count_even_odd_years(sets):
  even_count = 0
  odd_count = 0
  for key, elements in sets.items():
    if "AÑO" in elements: 
      year = int(build_num(elements["AÑO"]))
      if year % 2 == 0:
        even_count += 1
      else:
        odd_count += 1
  print(Back.LIGHTGREEN_EX + f"- La cantidad de conjuntos con años PAR son: {even_count}    " + Style.RESET_ALL)
  print(Back.LIGHTGREEN_EX + f"- La cantidad de conjuntos con años IMPAR son: {odd_count}  " + Style.RESET_ALL)

# Evalúa condiciones lógicas sobre los años de nacimiento y verifica a través de la key su return
def analyze_birth_years(sets, key):
  years = []
  for _, elements in sets.items():
    if "AÑO" in elements:
      year = int(build_num(elements["AÑO"])) 
      years.append(year)         
  if key == 13: 
    if all(year > 2000 for year in years):  
      print(Back.LIGHTCYAN_EX + "- Todos nacieron después del 2000, son los ¡GRUPO Z! " + Style.RESET_ALL)
    else:
      print(Back.LIGHTCYAN_EX + "- No todos nacieron luego del 2000, no son Grupo Z " + Style.RESET_ALL)
  elif key == 14: 
    leap_years = [year for year in years if is_leap_year(year)]
    if leap_years:
      print(Back.LIGHTGREEN_EX + f"- Tenemos un año especial, {', '.join(map(str, leap_years))} !" + Style.RESET_ALL)
    else:
      print(Back.LIGHTGREEN_EX + f"- No hay año bisiesto dentro de los conjuntos cargados " + Style.RESET_ALL)
           

#Esta función calcula el producto cartesiano entre años y edades.
def cartesian_product_age_year(sets, actual_set):
  current_year = datetime.now().year 
  age_set = set()  
  set_values = set()  
  if actual_set in sets and "AÑO" in sets[actual_set]:
    birth_years = int(build_num(sets[actual_set]["AÑO"]))
    age_set.add(current_year - birth_years)  
  if actual_set in sets and "SET" in sets[actual_set]:
    set_values.update(map(int, sets[actual_set]["SET"]))  
  cartesian_result = {(age, value) for age, value in product(age_set, set_values)}
  print(Fore.LIGHTGREEN_EX + f"- Primer conjunto (AÑO DE NACIMIENTO): {actual_set}={birth_years}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Valor del primer conjunto: {actual_set}={set_values}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Segundo conjunto (EDAD PROCESADA): Z={age_set}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Producto cartesiano: {actual_set}xZ={sorted(cartesian_result)}" + Style.RESET_ALL)
  return cartesian_result