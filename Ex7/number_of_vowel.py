def number_of_vowel(c: str):
  word_list = list(c)
  vowels = ["a", "e", "u", "i", "o"]
  vowel_number = 0

  for i in word_list:
    if i in vowels:
      vowel_number += 1
  return vowel_number

print(f"Nombre de voyelles de bonjour: {number_of_vowel("bonjour")}")
print(f"Nombre de voyelles de Salut: {number_of_vowel("Salut")}")
print(f"Nombre de voyelles de kjdtjff: {number_of_vowel("kjdtjff")}")
