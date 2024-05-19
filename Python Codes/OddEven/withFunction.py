def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = int(input("Enter number: "))
  if isEven(num):
    print(f'{num} is Even')
  else:
    print(f'{num} is Odd')