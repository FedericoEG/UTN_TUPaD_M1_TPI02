from colorama import Fore, Back, Style
from os import system as os_system
from platform import system as pl_system
from constants import OPTIONS

#Función que se encarga de alimentar la variable "sets" de manera automática
def seed():
  seeded_sets = {}
  seeded_sets["A"] = {"DNI": [3, 0, 6, 1, 1, 0, 9, 2], "SET": ["0", "1", "2", "3", "6", "9"]}
  seeded_sets["B"] = {"DNI": [3, 9, 3, 0, 3, 3, 5, 6], "SET": ["0", "3", "5", "6", "9"]}
  seeded_sets["C"] = {"YEAR": [2, 0, 1, 7], "SET": ["0", "1", "2", "7"]}
  seeded_sets["D"] = {"YEAR": [1, 9, 9, 5], "SET": ["1","5","9"]}
  return seeded_sets

#Función que se encarga de chequear si la cantidad de sets disponibles son suficientes para ejecutar la operación seleccionada
def check_sets(sets, required_sets):
  selected = list(required_sets * "_")
  abort = False
  clear_console()
  print(Fore.YELLOW + f"Debes seleccionar {f'{required_sets} conjuntos existentes' if required_sets > 1 else f'{required_sets} conjunto existente'} para realizar esta operación")
  print()
  print("Puedes volver al menu principal no ingresando nada." + Fore.RESET)
  print()
  while not abort and '_' in selected :
    s = upper_input(f"Introduce el conjunto #{selected.index('_')+1} (o ENTER para abortar): ").strip()
    if len(s) == 0 :
      abort = True
    elif s in sets :
      index = selected.index('_')
      selected[index] = s
    else :
      error(f"El conjunto {s} no existe.")
  return selected, abort

#Función que se encarga de devolver los elementos únicos de un array.
def sorted_unique_elements(elements):
  elements_without_char = []
  for element in elements:
    if element.isdigit():
      elements_without_char.append(element)
  unique_element_list = list(set(elements_without_char))
  unique_element_list.sort()
  return unique_element_list

#Función que se encarga de mostrar el mensaje de input y devuelve su valor capitalizado.
def upper_input(message):
	return str(input (message)).upper()

#Función que se encarga de devolver los valores de un array separados por comas y ordenados.
def join_and_sort(elements):
  elements.sort()
  return ",".join(elements)

#Función que se encarga de devolver los valores de un array como una concatenación de los mismos.
def build_num(elements):
  return ''.join(map(str, elements))

#Función que se encarga de transformar el valor string a un array de numeros.
def num_to_array(num):
  array = []
  for char in num:
    if char.isdigit():
      array.append(int(char))
  return array

#Función que se encarga de  detectar el sistema operativo en el que se está corriendo el programa y ejecuta la función apropiada para borrar la consola.
def clear_console():
    if pl_system() == "Windows":
        os_system('cls')
    else:
        os_system('clear')

#Función que se encarga de  generar un separador para la consola.
def separator(character = "-", qty = 60):
  separator = character * qty
  print(Fore.LIGHTMAGENTA_EX + f"{separator}" + Fore.RESET)

#Función que se encarga de lanzar un mensaje de error en la consola.
def error(message):
  clear_console()
  print(Fore.RED + message + Style.RESET_ALL)

#Funcion que se encarga de imprimir el mensaje de bienvenida, incluyendo una descripción de la aplicación y un listado detalladod e las operaciones posibles.
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

#Función que se encarga de mostrar las selecciones posibles y de comprobar que la selección realizada sea válida. Ya sea por recibir una opción no listada o que la cantidad de conjuntos no sea la correcta para la ejecución de la operación solicitada.
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

#Función que se encarga de imprimir los conjuntos que se le pasen por parámetro.
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

# Función que se encarga de determinar si un año es bisiesto
def is_leap_year(year):
  return True if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else False