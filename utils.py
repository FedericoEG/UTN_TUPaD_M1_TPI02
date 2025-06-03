from colorama import Fore, Back, Style

from os import system as os_system

from platform import system as pl_system

from constants import OPTIONS

#Es una función seeder porque me cansé de ingresar siempre data para poder probar.
def seed():
  seeded_sets = {}
  seeded_sets["A"] = {"DNI": [3, 1, 9, 1, 1, 0, 2, 6], "SET": ["0", "1", "2", "3", "6", "9"]}
  seeded_sets["B"] = {"DNI": [9, 5, 9, 5, 5, 9, 6, 6], "SET": ["4", "5", "6", "9"]}
  seeded_sets["C"] = {"DNI": [1, 1, 7, 8, 7, 7, 8, 7], "SET": ["1","6","7","8"]}
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

def build_dni(dni_elements):
  return ''.join(map(str, dni_elements))

#Esta función transforma el DNI string a un array de numeros.
def dni_to_array(dni):
  dni_array = []
  for char in dni:
    if char.isdigit():
      dni_array.append(int(char))
  return dni_array

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
  print(Fore.GREEN + f"Esta es una aplicación creada por alumnos de la comisión\n14 de la Tecnicatura Universitaria en programación\ndictada por la UTN. Corresponde al trabajo integrador de\nla materia MATEMÁTICA I. En esta se podrán ingresar\nnúmeros de documento para que sean convertidos a conjuntos\ny poder operar con los mismos.")
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
def insert_set(actual_sets, number_of_sets):
  separator()
  overrite = "no"
  set_name = input("Ingrese el nombre deseado para su conjunto. Se recomienda utilizar una letra MAYUSCULA: ")
  while set_name in list(actual_sets.keys()) and overrite == "no":
    overrite = input(Back.LIGHTYELLOW_EX + "El nombre seleccionado ya está en uso. Desea sobreescribir el conjunto? (si/no): " + Style.RESET_ALL)
    if overrite == "no":
      set_name = input("Ingrese el nombre deseado para su conjunto. Se recomienda utilizar una letra MAYUSCULA: ")
    else:
      overrite = "si"
  set_values = input("Ingrese su número de DNI sin puntos ni espacios para ser convertido en los valores del conjunto: ")
  actual_sets[set_name] = {}
  actual_sets[set_name]["DNI"] = dni_to_array(set_values)
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
    print(Fore.YELLOW + f"{key}=" + Fore.BLACK + Back.YELLOW + f"{{{join_and_sort(elements["SET"])}}}" + f" creado con el DNI: {build_dni(elements["DNI"])}" + Style.RESET_ALL)
    print()