def inverse(c: str):
    wordList = list(c)
    wordLength = len(wordList)
    for i in range(wordLength // 2):
      # Échange les caractères du début et de la fin
      wordList[i], wordList[wordLength - i - 1] = wordList[wordLength - i - 1], wordList[i]
    inverse_word = ''.join(wordList)
    return inverse_word

print(f"Salut inversé : {inverse('Salut')}")
