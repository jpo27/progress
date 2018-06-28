def name():
  username = input("What is your name? ")
  return username

def age():
  userage = input("What is your age? ")
  return userage

def message(age, name):
  if age <= 30:
    return "Young " + name
  else:
    return "Old " + name

def main():
  username = name()
  userage = int(age())
  print(message(userage, username))

if __name__ == "__main__":
  main()
