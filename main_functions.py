from colorama import Fore, Back, Style

from utils import sorted_unique_elements, join_and_sort, build_dni, clear_console, separator, show_sets

def union(set1_key, set1, set2_key, set2, print_answ = True):
  union = sorted_unique_elements(set1["SET"] + set2["SET"])
  if print_answ:
    clear_console()
    separator()
    print()
    print(Back.LIGHTGREEN_EX + f"La union de {set1_key}={{{join_and_sort(set1["SET"])}}} con {set2_key}={{{join_and_sort(set2["SET"])}}} es: {{{join_and_sort(union)}}}" + Style.RESET_ALL)
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
    print(Back.LIGHTGREEN_EX + f"La intersección de {set1_key}={{{join_and_sort(set1["SET"])}}} con {set2_key}={{{join_and_sort(set2["SET"])}}} es: {{{join_and_sort(intersection)}}}" + Style.RESET_ALL)
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
    print(Back.LIGHTGREEN_EX + f"La diferencia de {set1_key}={{{join_and_sort(set1["SET"])}}} con {set2_key}={{{join_and_sort(set2["SET"])}}} es: {{{join_and_sort(diff)}}}" + Style.RESET_ALL)
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
    print(Back.LIGHTGREEN_EX + f"La diferencia simétrica de {set1_key}={{{join_and_sort(set1["SET"])}}} con {set2_key}={{{join_and_sort(set2["SET"])}}} es: {{{join_and_sort(sis_difference)}}}" + Style.RESET_ALL)
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
    print(Back.LIGHTGREEN_EX + f"La suma de los dígitos de {set_key} => {build_dni(set["DNI"])} es: {sum_d}" + Style.RESET_ALL)
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
  print(Back.LIGHTGREEN_EX + f"La frecuendia de los dígitos de {set_key} => {build_dni(set["DNI"])} es:" + Style.RESET_ALL)
  print()
  for digit in digits:
    print(Fore.LIGHTGREEN_EX + f"* El {digit} se repite {f"{digits[digit]} veces" if digits[digit] > 1 else f"{digits[digit]} vez"}" + Style.RESET_ALL)
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
      print(Back.LIGHTYELLOW_EX + f"El conjunto {element} = {{{join_and_sort(actual_sets[element]["SET"])}}} tiene una diversidad numérica alta!" + Style.RESET_ALL)
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