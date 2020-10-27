def isPrime(num):
  minRange = 2
  maxRange = num

  for i in range(minRange, maxRange):
    if num % i == 0:
      return False

  return True

num = int(input())

print(isPrime(num))