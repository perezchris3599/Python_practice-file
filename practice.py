print("hello world")

#1-variables

date =21
pi =3.14
email = "kweeziperez712@gmail.com" 
eat = True

print(date)
print(eat)

#2-strings

footballer = input("who is your favourite footballer: ")
print("my favourite footballer is " + footballer)

#3-Logical operations

yourAge = input("How old are you? ")
birthYear = 2021 - int(yourAge)
print(birthYear)

#4-Inputs and logical operations
#numberA and numberB
#subtract numberB from numberA
#print the result

numberA = float(input("First: "))
numberB = float(input("Second: "))
sub = numberA-numberB

print("Result: " + str(sub))

if sub<0:
   print("Negative Number")
else:
    print("Positive Number")

perezc = "I love hacking and i learn fast"
print(perezc.upper())
print(perezc.lower())
print(perezc.find('d'))
print(perezc.replace('love', 'like'))
print(perezc.find("hacking"))

#5-Arithmetic operations
x = 5
y = 11
x+=y
x-=y
print(x)

#6-Comparisons and Logical operations

x = 5==4
print(x)
rent = 550
print(rent>50 and rent<1000 and rent!=400)

#7-if statements
carSpeed = 101
if carSpeed > 100:
   print("You are driving too fast")
elif carSpeed < 20:
   print("You are driving too slow. this is a highway")
else:
    print("Your speed is good")
print("Ready")

#8-loops
i =0
while i<=5:
    print(i)
    print(i*'i')
    i=i+1

for loops
temperatures = [67, 30, 70, 43, 91]

for item in temperatures:
    print(item)
numbers = range(10,100,5)#printing numbers between 10 and 100 with a difference of five numbers
for number in numbers:
    print(number)

#9-data structures
techlist = ["apple", "microsoft", "samsung", "dell", "hp"]
print(techlist[0:2])
techlist[0] = "Tesla"
print(techlist)
techlist.remove("samsung")
techlist.insert(3, "tesla")
print(len(techlist))#to print the length of the techlist
print("microsoft" in techlist)
techlist.clear() #this is to clear everything in the list
print(techlist)

#10-dictionaries
fruits = {'banana':0.49, 'orange':1.5, 'apple':1.09}
fruits['banana']= 2.60
print(fruits['orange']) #to display prices of particular fruits
fruits['melon'] =3
print('banana')
print(fruits)

#11-python void functions
def homework_task(language, task):
    print("your homework task: ")
    print(task + "in " + language)

print("start")

homework_task("java", "write a function")

print("End")

#12-Return functions
def path(v,t):
    print(v*t)

print(path(30, 60))

degree = input("what is your degree level, Bachelor, Masters or Phd? ")
experience = input("how many years of experience do you have? ")

if degree == "Masters" or degree == "Phd" or degree == "masters" or degree == "phd":
    if int(experience) >= 2:
        print("You are accepted for the interview.")
    else:
        print("You dont have enough experience.")
else:
    print("You dont have the required degree")

#13-exceptions
try:
    items = int(input("Type a number of items: "))
    total =30
    price_per_item = total/items
    print(items)
except ValueError:
    print("Your value is not an integer")
except ZeroDivisionError:
    print("you cannot divide by zero")

#14-Classes, objects and methods.
class animal:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def run(self):
        print("Running...")
    def eat(self):
        print("eating...")

dog = animal('poodle', 'white')

print(dog.breed)

#15-classes
class line:
    def __init__(self, length, x, y):
        self.length = length
        self.x = x
        self.y = y
   def draw(self):
       print("Drawing...")
   def display(self):
        print("Display")

line1 = line(5, 1,1)
print(line1.length)
line1.draw()

#16-Inheritence
class human():
    def speak(self):
        print("Speaking...")

class German(human):
    pass

class French(human):
    pass

stefan = French()
stefan.speak()

#17-modules

import convert
from convert import m_to_cm

print(m_to_cm(2))


