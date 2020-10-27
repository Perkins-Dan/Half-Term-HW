userInput = input()

listInput = list(userInput)
compOutput = []

vowels = ['a', 'e', 'i', 'o', 'u']

# loops through all the letters in the users input
for letter in listInput:
  check = True

  # loops through all the vowels
  for vowel in vowels:

    # checks too see if each vowel = the letter
    if letter == vowel:

      # passes -> assigns check to false, no append needed
      check = False
  
  # checks to see if check is still true
  if check == True:

    # passes -> check is true, the letter can be appended
    compOutput.append(letter)

# outputs compOutput list as a string
print(''.join(compOutput))