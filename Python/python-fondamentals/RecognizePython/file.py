#variable declaration type primitive
num1 = 42  #initialize a integer number
num2 = 2.3 #initialize a float number
boolean = True #initialize boolean
string = 'Hello World' #initialize string

#composite data types initialization
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #type dictionary
fruit = ('blueberry', 'strawberry', 'banana') #this is a tuple

print(type(fruit)) #this line prints the type of data in fruit
print(pizza_toppings[1]) #this line prints the element of pizza_toppings in possition 1 which is Sausage
pizza_toppings.append('Mushrooms') #in this way we add an new element in the list
print(person['name']) #access the value with the name as a key
person['name'] = 'George' #change the name value from Jhon to George

"""adds another element (key:value)
in dictionary besides the other elements"""

person['eye_color'] = 'blue'  

print(fruit[2]) #it prints the element in possition 2 in the tuple named fruit

#if else conditions, it executes the else condition because the num1<45
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""if else conditions,
it executes the else condition because 
the length of the string doesn'n meet the if or elif condition"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#for loop it prints the numbers who start from 0 incremented by 1 and stops to 4
for x in range(5):
    print(x)
#for loop it start at number 2 incremented by one and stops at 4   
for x in range(2,5):
    print(x)
#for loop it start at number 2 incremented by 3 and stops at 8 without including 10     
for x in range(2,10,3):
    print(x)

#while loop
x = 0 #start at 0
while(x < 5): #while is less than 5
    print(x) #prints all the values
    x += 1 #increments by 1

pizza_toppings.pop() #it delets the last element from the list
pizza_toppings.pop(1) #it delets element in possiton 1 from the list

print(person) #prints the person dictionary with key:values in it

"""delets the eye_color element from the dictionary
and then prints the person without that element"""
person.pop('eye_color')
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if it meets the if condition it continues and then prints the mesage 3 times
        continue
    print('After 1st if statement')
    if topping == 'Olives': #and when the topping is equal to Olives it breaks the loop
        break

#this is a function which prints a message in rank 10 at the moment it is called
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #this is how we call a function, it is not going to be executed till this moment

#this is a function with a given parameter x
def print_hello_x_times(x):
    for num in range(x): 
        print('Hello')

print_hello_x_times(4) #we call the functin and give him a argument instead of the parameter x to be executed

def print_hello_x_or_ten_times(x = 10): #here we have a function with a given parameter x=10
    for num in range(x): #the for loop is going to be executed in range of the given parameter
        print('Hello')

print_hello_x_or_ten_times() #we call the function and it is goig to print the message 10 times (from 0 to 9)
print_hello_x_or_ten_times(4) #the function is going to be excecuted 4 times thats the argument given by us


"""
Bonus section
"""

# print(num3)
# this is a name error we dont have a variable num3 first we daclare it then we can print it
num3= 3
print(num3)
# num3 = 72
num3= 72 #here we change the value of the variable num3
# fruit[0] = 'cranberry'
fruit[0] = 'cranberry' #type error we can not change the element in a tuple
# print(person['favorite_team'])
print(person['favorite_team']) #KeyError: 'favorite_team' we dont have such a key in our dictionary
# print(pizza_toppings[7])
print(pizza_toppings[7]) #IndexError: list index out of range, this list is in rage 4
#  print(boolean)  
   print(boolean) #IndentationError: unexpected indent

# we can't add or delete the elements in a tuple, the tuple is unchangeable
fruit.append('raspberry')
fruit.pop(1)