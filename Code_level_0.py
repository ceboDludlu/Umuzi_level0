import math

#task 0.1
value_of_x = 0
value_of_y = 1

print(value_of_x)
print(value_of_y)

x = value_of_x +3
y = value_of_y + x

print(x)
print(y)

#task 0.2
x_ = 1+1*2
y_ = (1+1)*2
z_ = 1+(1*2)
a_ = 1+1*2/2
b_ = (1+1*2)/2

print(x_)
print(y_)
print(z_)
print(a_)
print(b_) 

#task 3.0
hello = "Hello Tshepo"
print(hello)

#task 4.0
even_or_odd = int(input("enter the number:"))
if even_or_odd % 2 == 0:
    print("Even") 
else:
    print("Odd")   

#task5.0
a = float(input("input first number: "))
b = float(input("input second number: "))
c = float(input("input third number: "))

a = float((c**2) - (b**2))
h = math.sqrt(a)
area = float(0.5*(b*h))
print(area)

#task6.0
r = int(input("input first digit: "))
s = int(input("input second digit: "))
t = int(input("input third digit: "))

print(max(r, s, t))

#task 7.0
w = float(input("input value of celsius: "))
f = float(input("input value of fahrenheit: "))

fahrenheit = float((w - 32) * 5/9)
celsius = float((f *9/5) + 32)
print(fahrenheit, "fahrenheit")
print(celsius, "celsius")

#task 8.0
hours = int(input("Enter hours value: "))
minutes = hours * 60
print(minutes, "minutes")

minutes_ = int(input("enter minutes value: "))
hours_ = minutes_ / 60
print(hours_ ,"hours")

#task9.0
str_input = input("input a string: ")
for vowels in 'aeiou':
    if vowels in str_input :
        print(vowels)

#task10.0
word1 = input("input first word: ")
word2 = input("input second word: ")
s1 = set(word1)
s2 = set(word2)
common_letters = list(s1 & s2)
print(common_letters)


