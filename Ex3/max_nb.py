def max_nb(n:int | float, m:int | float, p:int | float) -> int | float:
  max = n
  if max <= m and m >= p:
    max = m
  if max <= p:
    max = p
  return f"le max est {max}"

print(max_nb(90, 190, 99))
print(max_nb(90, 190, 190))
print(max_nb(90, 10, 9))
print(max_nb(37.5, 19.3, 99.9))