def collatz(number):
    if (number%2) == 0:
        print(number//2)
        return int((number//2))
    elif number == 1:
        print(number)
        return int(number)
    elif (number%2) == 1:
        print(3*number + 1)
        return int((3*number + 1))

try:
    n = int(input("Enter a number: "))
except ValueError:
    print('Enter an integer value only')

while n != 1:
    n = collatz(n)
