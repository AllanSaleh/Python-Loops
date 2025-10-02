import random

secret_number = random.randint(1,100)

guess = None

attempts = 0
max_attempts = 5

while attempts < max_attempts:
  guess = int(input("Guess the number (between 0 - 100): "))
  attempts +=1

  if guess < secret_number:
    print(f"Too low! Try a higher number. You have {max_attempts - attempts} attempts left.")
  elif guess > secret_number:
    print(f"Too high! Try a lower number. You have {max_attempts - attempts} attempts left.")
  else:
    print("🎉 You guessed it!")
    break

if guess != secret_number:
  print("Out of attempts. The number was ", secret_number)