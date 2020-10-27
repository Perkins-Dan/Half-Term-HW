from random import randint

nums = []

while True:
  gen = str(randint(1,9))
  check = True
  
  # Checks If List is empty
  if not nums:

    # Passes -> No need for checks, can append number
    nums.append(gen)

  else:

    # Fails -> Needs more checks
    for num in nums:

      # Checks if each number in the list is equal
      if num == gen:

        # Passes -> Assigns check to false (It has failed)
        check = False

    if check == True:

      # Fails -> Can append the number
      nums.append(gen)

  # Checks to see if list is 4 numbers long -> Breaks while loop if = 4
  if len(nums) == 4:
    break

# Outputs number as a string
print(''.join(nums))