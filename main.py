from main_functions import count_years, union, intersection, difference, sis_difference, digits_addition,digits_count, digits_analize, delete_set, verify_births, verify_cartesian_product

from utils import show_welcome, options_menu, insert_set, show_sets, error, upper_input,check_sets, seed

from constants import OPTIONS

#Inicial values required
sets = seed()
number_of_sets = len(list(sets.keys()))
option = None

show_welcome()

while option == None or OPTIONS[option]["key"] != 0:
  option = options_menu(number_of_sets)

  if OPTIONS[option]["key"] == 1 or OPTIONS[option]["key"] == 11:
    number_of_sets = insert_set(sets, number_of_sets, key = OPTIONS[option]["key"])

  elif OPTIONS[option]["key"] == 2:
    show_sets(sets)

  elif OPTIONS[option]["key"] == 3:
    [set1, set2], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      union(set1, sets[set1], set2, sets[set2])

  elif OPTIONS[option]["key"] == 4:
    [set1, set2], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      intersection(set1, sets[set1], set2, sets[set2])

  elif OPTIONS[option]["key"] == 5:
    [set1, set2], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      difference(set1, sets[set1], set2, sets[set2])

  elif OPTIONS[option]["key"] == 6:
    [set1, set2], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      sis_difference(set1, sets[set1], set2, sets[set2])

  elif OPTIONS[option]["key"] == 7:
    [set1], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      digits_addition(set1, sets[set1])

  elif OPTIONS[option]["key"] == 8:
    [set1], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      digits_count(set1, sets[set1])

  elif OPTIONS[option]["key"] == 9:
    if number_of_sets > 0:
      digits_analize(sets)
    else:
      error("Debe haber al menos un conjunto cargado para poder hacer este análisis. Puedes usar la opción ingresar conjunto (IC) para cargar un DNI/CONJUNTO")

  elif OPTIONS[option]["key"] == 10:
    [set1], abort = check_sets(sets, OPTIONS[option]["sets_required"])
    if not abort :
      delete_set(set1, sets)

  elif OPTIONS[option]["key"] == 12:
    if len(sets) != 0:
      count_years(sets)
    else:
      error("Debes tener cargados los conjuntos antes de realizar la operación\nSi necesitas ingresar un conjunto usa la opción para realizarlo (IA)")

  elif OPTIONS[option]["key"] == 13 or OPTIONS[option]["key"] == 14:
    if len(sets) != 0:
      verify_births(sets, OPTIONS[option]["key"])
    else:
      error("Debes tener cargados los conjuntos antes de realizar la operación\nSi necesitas ingresar un conjunto usa la opción para realizarlo (IA)")

  elif OPTIONS[option]["key"] == 15:
    if len(sets) != 0:
      verify_cartesian_product(sets)
    else:
      error("Debes tener cargados los conjuntos antes de realizar la operación\nSi necesitas ingresar un conjunto usa la opción para realizarlo (IA)")