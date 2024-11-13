from utils.inverse_word import inverse

def is_palindrome(c: str) -> bool:
  c_inverse = inverse(c)
  print(f"Mot inversé : {c_inverse}")
  if c == c_inverse:
    return True
  else:
    return False

print(f"Palindrome de poule ? {is_palindrome("poule")}")
print(f"Palindrome de kayak ? {is_palindrome("kayak")}")