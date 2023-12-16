#1.Basic-print all itegers from 0-150
for integers in range (151):
    print(integers)


#2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range (5,1000,5):
    print(x)


#3.Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range (1,100):
    if  x%10==0:
        print("Coding Dojo")
    elif x%5==0:
        print("Coding")
    else:
        print(x)

#4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for integers in range (500000):
    if integers%2!=0:
        sum+= integers
print("The final sum is:", sum)

#5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for positive_numbers in range(2018,0,-4):
    print(positive_numbers)

"""6.Flexible Counter - Set three variables: lowNum, highNum, mult.
 Starting at lowNum and going through highNum, print only the integers 
 that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3,
 the loop should print 3, 6, 9 (on successive lines)"""

lowNum=3
highNum=36
mult=6
for number in range (lowNum, highNum+1):
    if number %mult ==0:
        print(number)
