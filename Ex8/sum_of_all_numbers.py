def sum_of_all_number(lst: list):
  sum = 0
  for i in lst:
    sum += i
  # for i in range(len(lst)):
  #   sum += lst[i]
  return round(sum, 2)

purchases = [23.99, 110, 10, 43.65]

print(f"La somme de la liste est {sum_of_all_number(purchases)}")