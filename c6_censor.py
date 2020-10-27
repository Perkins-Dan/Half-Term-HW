def censor(text, word):
  censorLen = len(word)
  censorList = []
  for i in range(censorLen):
    censorList.append('*')
  
  censorString = ''.join(censorList)

  newString = text.replace(word, censorString)

  return newString

text = input('Enter a sentence: ')
word = input('Enter the word: ')

newText = censor(text, word)

print(newText)