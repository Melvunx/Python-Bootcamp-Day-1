def anagram(str1: str, str2: str) -> bool:
  word_list_1 = list(str1.lower())
  word_list_2 = list(str2.lower())
  
  if not len(word_list_1) == len(word_list_2):
    return False
  
  for i in word_list_1:
    if i in word_list_2:
      word_list_2.remove(i)
      if word_list_2 == []:
        return True
    else:
      return False

print(f"Anagram true: {anagram("Poule", "loupe")}")
print(f"Anagram false: {anagram("Kayakist", "kayak")}")
print(f"Anagram false: {anagram("happy", "kappy")}")