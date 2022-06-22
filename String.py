s = "vivek"
print(s)
print(len(s))

s = "My name is " + s
print(s)

print(s[5])

print(s[2:7])

print(s[::-1])

print(s[::3])

name = "My name is vivek"
print(name.split())
print(name.upper())

print("my name is %s " % 'vivek')
print("my name is %s and i'm staying in %s " % ('vivek ', 'chennai '))
print("my name is %r and i'm staying in %s " % ('vivek ', 'chennai '))


a = 100
b = 500

print("the total value is {} ".format(a + b))
print("the total value is {} ".format(a / b))

print(f"the total value is {a - b} ")

num = 10.5214161644
print("the total length of the number is : {0:10.5f} ".format(num))
print(f"the total length of the number is  : {num :10.6f} ")
