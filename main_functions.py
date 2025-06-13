from colorama import Fore, Back, Style
from itertools import product
from datetime import datetime

from utils import is_leap_year, num_to_array, sorted_unique_elements, join_and_sort, build_num, clear_console, separator, show_sets, upper_input

def union(set1_key, set1, set2_key, set2, print_answ = True):
  union = sorted_unique_elements(set1["SET"] + set2["SET"])
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La union de {set1_key}={{{join_and_sort(set1['SET'])}}} con {set2_key}={{{join_and_sort(set2['SET'])}}} es: {{{join_and_sort(union)}}}" + Style.RESET_ALL)
    print()
  else:
    return union

def intersection(set1_key, set1, set2_key, set2, print_answ = True):
  intersection = []
  if len(set1["SET"]) > len(set2["SET"]):
    long = set1["SET"].copy()
    short = set2["SET"].copy()
  else:
    long = set2["SET"].copy()
    short = set1["SET"].copy()
  for element in long:
    if element in short:
      intersection.append(element)
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La intersección de {set1_key}={{{join_and_sort(set1['SET'])}}} con {set2_key}={{{join_and_sort(set2['SET'])}}} es: {{{join_and_sort(intersection)}}}" + Style.RESET_ALL)
    print()
  else:
    return intersection

def difference(set1_key, set1, set2_key, set2, print_answ = True):
  diff = set1["SET"].copy()
  for element in set2["SET"]:
    if element in diff:
      diff.remove(element)
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La diferencia de {set1_key}={{{join_and_sort(set1['SET'])}}} con {set2_key}={{{join_and_sort(set2['SET'])}}} es: {{{join_and_sort(diff)}}}" + Style.RESET_ALL)
    print()
  else:
    return diff

def sis_difference(set1_key, set1, set2_key, set2, print_answ = True):
  union_of_sets = union(set1_key, set1, set2_key, set2, False)
  intersection_of_sets = intersection(set1_key, set1, set2_key, set2, False)
  sis_difference = difference("union", {"SET": union_of_sets}, "intersection", {"SET": intersection_of_sets}, False)
  print("🐍 File: UTN_TUPaD_P1_TP_INTEGRADOR_2/utils.py | Line: 170 | sis_difference ~ sis_difference",sis_difference)
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La diferencia simétrica de {set1_key}={{{join_and_sort(set1['SET'])}}} con {set2_key}={{{join_and_sort(set2['SET'])}}} es: {{{join_and_sort(sis_difference)}}}" + Style.RESET_ALL)
    print()
  else:
    return sis_difference

def digits_addition(set_key, set, print_answ = True):
  sum_d = 0
  for element in set["DNI"]:
    sum_d += element
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La suma de los dígitos de {set_key} => {build_num(set['DNI'])} es: {sum_d}" + Style.RESET_ALL)
    print()
  else:
    return sum_d

def digits_count(set_key, set):
  digits = {}
  digits_to_analize = set["DNI"].copy()
  digits_to_analize.sort()
  for digit in digits_to_analize:
    if digit in digits.keys():
      digits[digit] += digits[digit]
    else:
      digits[digit] = 1
  clear_console()
  separator()
  print()
  print(Back.LIGHTGREEN_EX + f"La frecuendia de los dígitos de {set_key} => {build_num(set['DNI'])} es:" + Style.RESET_ALL)
  print()
  for digit in digits:
    print(Fore.LIGHTGREEN_EX + f'* El {digit} se repite {f"{digits[digit]} veces" if digits[digit] > 1 else f"{digits[digit]} vez"}' + Style.RESET_ALL)
  print()

def digits_analize(actual_sets):
  all_digits = []
  digits_in_all_sets = []
  clear_console()
  separator()
  print()
  for element in actual_sets:
    all_digits += actual_sets[element]["SET"]
    if len(actual_sets[element]["SET"]) > 6:
      print(Back.LIGHTYELLOW_EX + f"El conjunto {element} = {{{join_and_sort(actual_sets[element]['SET'])}}} tiene una diversidad numérica alta!" + Style.RESET_ALL)
      print()
  uniq_digits = list(set(all_digits))
  uniq_digits.sort()
  for digit in uniq_digits:
    for key in actual_sets.keys():
      if digit in actual_sets[key]["SET"]:
        digits_in_all_sets.append(digit)
  for digit in uniq_digits:
    if digits_in_all_sets.count(digit) == len(actual_sets.keys()):
      print(Back.LIGHTGREEN_EX + f"El número {digit} se encuentra en todos los conjuntos." + Style.RESET_ALL)
  print()

def delete_set(set_key, actual_sets):
  actual_sets.pop(set_key)
  clear_console()
  separator()
  print(Back.LIGHTRED_EX + Fore.RED + f"El conjunto fue eliminado exitosamente!" + Style.RESET_ALL)
  print()
  show_sets(actual_sets, False)

def count_years(sets):
  clear_console()
  separator()
  print()
  count_even_odd_years(sets)
  print()

def verify_births(sets, key):
  clear_console()
  separator()
  print()
  analyze_birth_years(sets, key)
  print()

def verify_cartesian_product(sets):
  new_set = input("Por favor, ingresa el nómbre del conjunto en mayúscula, que deseas verificar: ")
  clear_console()
  separator()
  print()
  new_set = new_set.upper()
  if new_set in sets:
    if "YEAR" in sets[new_set]:
      cartesian_product_age_year(sets, new_set)
    else:
      print(Fore.YELLOW + f"- El conjunto '{new_set}' no existe en la base de AÑOS DE NACIMIENTO." + Style.RESET_ALL)
      print(Fore.YELLOW + "- Utilizá el comando (VC) para visualizar los conjuntos cargados en el sistema." + Style.RESET_ALL)
  else:
    print(Fore.YELLOW + f"- El conjunto '{new_set}' no existe en la base de AÑOS DE NACIMIENTO." + Style.RESET_ALL)
    print(Fore.YELLOW + "- Utilizá el comando (VC) para visualizar los conjuntos cargados en el sistema." + Style.RESET_ALL)
  print()

#Función que se encarga de ingresar un nuevo conjunto al listado de conjuntos. Ya se encarga de normalizar los elementos ingresados para que sean únicos.
def insert_set(actual_sets, number_of_sets, key):
  if key == 1:
    key_name = "DNI"
  else:
    key_name = "AÑO DE NACIMIENTO"
  separator()
  overrite = "no"
  set_name = upper_input("Ingrese el nombre deseado para su conjunto. Se recomienda utilizar una letra MAYUSCULA: ")
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
    actual_sets[set_name]["YEAR"] = num_to_array(set_values)
    actual_sets[set_name]["SET"] = sorted_unique_elements(list(set_values))
  number_of_sets = len(actual_sets.keys())
  clear_console()
  separator()
  print(Back.LIGHTGREEN_EX + Fore.GREEN + f"El conjunto fue agregado exitosamente!" + Style.RESET_ALL)
  print()
  show_sets(actual_sets, False)
  return number_of_sets

# Función que se encarga de contar la cantidad de años pares e impares hay en los conjuntos con key="YEAR"
def count_even_odd_years(sets):
  even_count = 0
  odd_count = 0
  for key, elements in sets.items():
    if "YEAR" in elements:
      year = int(build_num(elements["YEAR"]))
      if year % 2 == 0:
        even_count += 1
      else:
        odd_count += 1
  print(Back.LIGHTGREEN_EX + f"- La cantidad de conjuntos con años PAR son: {even_count}    " + Style.RESET_ALL)
  print(Back.LIGHTGREEN_EX + f"- La cantidad de conjuntos con años IMPAR son: {odd_count}  " + Style.RESET_ALL)

  # Función que se encarga de evaluar condiciones lógicas sobre los años de nacimiento y verifica a través de la key su return
def analyze_birth_years(sets, key):
  years = []
  for _, elements in sets.items():
    if "YEAR" in elements:
      year = int(build_num(elements["YEAR"]))
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

#Función que se encarga de calcular el producto cartesiano entre años y edades.
def cartesian_product_age_year(sets, actual_set):
  current_year = datetime.now().year
  age_set = set()
  set_values = set()
  birth_years = 0
  if actual_set in sets and "YEAR" in sets[actual_set]:
    birth_years = int(build_num(sets[actual_set]["YEAR"]))
    age_set.add(current_year - birth_years)
  if actual_set in sets and "SET" in sets[actual_set]:
    set_values.update(map(int, sets[actual_set]["SET"]))
  cartesian_result = {(age, value) for age, value in product(age_set, set_values)}
  print(Fore.LIGHTGREEN_EX + f"- Primer conjunto (AÑO DE NACIMIENTO): {actual_set}={birth_years}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Valor del primer conjunto: {actual_set}={set_values}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Segundo conjunto (EDAD PROCESADA): Z={age_set}" + Style.RESET_ALL)
  print(Fore.LIGHTGREEN_EX + f"- Producto cartesiano: {actual_set}xZ={sorted(cartesian_result)}" + Style.RESET_ALL)
  return cartesian_result