
#Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)

#Print all even numbers between 1 and 20.
for i in range(0,21,2):
    print(i)

#Print the characters of the string "Python" one by one using a loop.
s="python"
for i in s:
    print(i)

#Print the sum of numbers from 1 to 100.
s=0
for i in range(1,101):
    s=s+i 
print(s)

#Print multiplication table of 5 (like 5 x 1 = 5, ... 5 x 10 = 50).
n=5
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#Print all elements of a list using a loop.
List=["apple", "banana", "cherry"]
for i in List:
    print(i)


#Print only the vowels from the string "education" using a loop.
n="education"
v={'a','e','i','o','u'}
for i in n:
    if i in v:
        print(i)


#Count how many times the letter 'a' appears in the string "banana" using a loop.
s="banana"
c=0
for i in s:
    if i=='a':
        c=c+1 
print(c)


#Print numbers from 10 to 1 using a loop (reverse order).
for i in range(10,0,-1):
    print(i)

#Ask the user to enter 5 numbers using a loop and print their sum.v=['a','e','i','o','u']
n=list(map(int,input().split(" ")))
s=0
for i in n:
    s=s+i 
print(s)
