from utils.sum_of_all_number import sum_of_all_number

def median(element: list | set | tuple):
  result = sum_of_all_number(element) / len(element)
  return round(result, 2)

print(f"Res list : {median([23, 65, 93.4, 28, 284.54])}")
print(f"Res tuple : {median((23, 65, 28, 284.54))}")
print(f"Res set : {median({23, 65, 93.4, 28})}")