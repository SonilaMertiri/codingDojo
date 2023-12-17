#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#output is 5. When we call the function (line 4) is going to print what is in return (line 3).



#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#NameError number_of_days_in_a_week_silicon_or_triangle_sides() is not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#the output is 5 what is returned first, as we know the function is going to stop as it meet the first return


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#the output is 5. Same think as above when we have a return in a function, after that return no line in that function code-block is going to be executed


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#is going to be printed 5 once for the print inside the function and as the function has not a return we dont have another output.


#6
def add(b,c):
    print(b+c)
    # return b+c
print(add(1,2) + add(2,3))
#we call the function two times and the output is 3 for the first call and 5 for the second, then we have a type error because we didn'n return anything.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#the output is going to be 25, we convert two integers in strings and than concatenate them at the return


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#the output is going to be 100 for the print inside the function and 10 for the return that fulfills the condition else in our case


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""the output is 7 in the first call, 14 in the second call
and in the third call actually we call the function twice
and then concatenate whatever the output of each one is, so 7+14=21 is the output for the third print"""


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#the output is 8, the first return is going to be executed


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
"""the output is 500 for the print in line 104, than again 500 for the print in line 109
after that we call the function in line 110 and the output is 300 because we returned b
than again line 111 prints the 500"""


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#the output is 500, 500, 300, 300. in difference from example abouve, here at line 126 we change the b=foobar() than print whatever is returned so 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#here we call only foo function so the output is 1 for the print in line 132, 3 because we call bar() inside the foo function and 2 for line 134

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#the output is 1 for line 142, than we call bar who prits 3 and returns 5. than we call foo at line 149 and print what is returned from foo so 10
#so output is 1,3,5 10