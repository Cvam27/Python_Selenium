def fibonacci():
    a, b = 0, 1

    for _ in range(10):
        print(a)
        a = b
        b = a + b

# fibonacci()
#######################################################

def isPrimeNumber(number):
    if number % 2 == 0:
        print("Not Prime")
    else:
        print("prime")


# isPrimeNumber(int(input("enter a number ")))
#######################################################

def reverseNumber(numb):
    revers = int(str(numb)[::-1])
    return  revers, type(revers)


numbr = 12345
# print(reverseNumber(numbr))
#######################################################

def palindrome_string(data):
    return True if data == data[::-1] else False

# print(palindrome("madamd")) # False
# print(palindrome("madam")) # True
#######################################################

def palindrome_number(data):
    return True if str(data) == str(data)[::-1] else False

# print(palindrome_number(12321))
#######################################################

result = {}
def occ(data):
    for char in data:
        if char in result:
            result[char] = result[char] +1
        else:
            result[char] = 1

    for key,val in result.items():
        print(key, val)


name = "banana"
# occ(name)
#######################################################

def printOnlyNumbers(data):
    onlyNumbr = ""
    for ch in data:
        if ch.isdigit():
            onlyNumbr += ch

print(printOnlyNumbers("shivam 100"))