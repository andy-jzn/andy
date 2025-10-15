# --- Variables and Data Types ---

a=10
print(a)
print(type(a)) #integer, whole number with no decimals

b=1.5
print(b)
print(type(b)) #float, has decimals

c=3j
print(c)
print(type(c)) #complex, has a real part and an imaginary

d="hello"
print(d)
print(type(d)) #string, sequence of characters

e=[1, 2, 3]
print(e)
print(type(e)) #list, collection of ordered elements

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #dict, collection of elements in order who come in key value pairs and each key is unique 

g = (1, 2)
print(g)
print(type(g)) #tuple, list that once created you cannot add or change the elements

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #list, collection of ordered elements

i = True
print(i)
print(type(i)) #bool, can only have two values, either true or false

j = None
print(j)
print(type(j)) #nonetype, represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) #list, collection of ordered elements

l= str(14)
print(l)
print(type(l)) #str, sequence of characters

m = 1e4
print(m)
print(type(m)) #float, number with decimal places, scientific notation for 10000.0

#1. How many different data types did you find? --> 9
#2. List all the data types you found. --> int, float, complex, str, list, dict, tuple, bool, NoneType
#3. What variables have the same data types?
    #int: a, m (m is stored as float but represents a number)
     #float: b
     # complex: c
     # str: d, l
     # list: e, h, k
     # dict: f
     # tuple: g
     # bool: i
     # NoneType: j
#4. What was the data type of l? Why is it not an integer? What does str() do? --> str() converts its input intp a string. ie. l is a string because we wrapped 14 inside str()
#5. Look up one more data type not given above. Repeat the same procedure. 
n = {1, 2, 3}
print(n)
print(type(n)) # set, collection of unique elements, mutable


#---3.2 Booleans---
print(10>9) #True, 10 is greater than 9
print(10==9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, non empty strings evaluate to True
print(bool(123)) #True, non-zero numbers evaluate to True
print(["apple", "cherry", "banana"]) #True, non-empty lists evaluate to True
print(bool(True)) #True, the value is True
print(bool(False)) #False, the value is False
print(bool(0)) #False, zero evaluates to False
print(bool("")) #False, empty string evaluates to False
print(bool(" ")) #True beacuse it is not empty, it contains a space
print(bool(())) #False, empty tuple evaluates to False
print(bool([])) #False, empty list evaluates to False
print(bool({})) #False, empty dictionary evaluates to False
print(bool(True and False)) #False, because both must be True for "and" to be true
print(bool(True and True)) #True, both conditions are true
print(bool(False and False)) #False, both are false
print(bool(True or False)) #True, at least one condition is true
print(bool(True or True)) #True, at least one is true
print(bool(False or False)) #False, neither condition is True
print(bool(not(False))) #True, not(False) becomes true
print(bool(not(True))) #False, not(true) becomes false 

#QUESTIONS
#What pattern do you notice about expressions returning True or False? --> Non-empty values (strings, lists, numbers) are True; empty values and zero are False. 
# Logical operators (and, or, not) follow standard logic rules

#Which expression surprised you about its result?
# bool(" ") was surprising, because even a space counts as non-empty, so it evaluates to True

# Create an expression, not given above, that will return True. Why is it True?
print(9>=9) # True, because 9 is equal to 9
# Create an expression, not given above, that will return False. Why is it False?
print(7 < 2)   # False, because 7 is not less than 2

#---3.3 Operators---
##3.3.1 --> Arithmetic operators

print(10+5) #15, + performs addition
print(10-5) #5, - perdorms subtraction
print(2*4) #8, * performs multiplication
print(6/3) #2.0 performs division, returns a float
print(5%2) #1, modulus returns the remainder of the division
print(3**2) #9, exponent and assign (3 got squared)
print(15//2) #division, return an integer

##3.3.2 Comparison Operators
print(5==0) #False, == Equal to
print(10!=10) #False != not equal
print(2<5) #True, < less than
print(12>5) #True > greater than
print(5<=6) #True, <= less than or equal
print(1>=10) #False, greater than or equal

##Assignment Operators
x=5
x+=5
print(x) #10, x=x+5 =10

x-=4
print(x) #6, x=x-4 =6 (x being 10)

x*=3
print(x) #18, x*3=18 (x being 6)

##3.3.4 Logical Operation
#What does the operator and do? Write an expression that results in True. Write an expression that results in False.
print(True and True)   # True, because both are True
print(True and False)  # False, because one is False

#What does the operator or do? Write an expression that results in True. Write an expression that results in False.
print(True or False)   # True, one is True
print(False or False)  # False, both are False

#What does the operator not do? Write an expression that results in True. Write an expression that results in False.
print(not(True))       # False, flips True → False
print(not(False))      # True, flips False → True

#More Questions:
#1. What is the difference between / and //?
#/ returns a float, whereas // returns the quotient as an integer

#2. What is the difference between % and //?
#% gives the remainder, whereas // returns the quotient

#3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
#% is the modulus operator
print(10%3) #returns 1

#4. How do assignment operators work?
#They update a variable by combining it with another value.


#---3.4 Strings
my_string ="hello"

print(my_string) #hello
print(my_string[0]) #h, Access characters by index 
print(my_string[1]) #e, Access characters by index
print(my_string[2])#l, Access characters by index
print(my_string[3])#l, Access characters by index
print(my_string[4]) #o, Access characters by index
print(my_string[-1]) #o, Negative indexing -1 gives last character
print(my_string[1:3]) #el, Slicing [start:end] → grabs substring (end index not included)
print(my_string[0:5:2]) #hlo, Slicing with step [start:end:step] (characters at index 0, 2, 4)
print(len(my_string)) #5, length of string

print(my_string + "goodbye") #hellogoodbye, string concentration 
print(my_string * 7) #hellohellohellohellohellohellohello, string repetition 7 times

#QUESTIONS
#1. Define slicing:
# Slicing = extracting a portion of a string using [start:end:step].

# 2. Using commas in print
name = "Oski"
print("Hello, my name is", name)  
# Prints: Hello, my name is Oski
# The comma automatically adds a space.

# 3. Using f-strings
print(f"Hello, my name is {name}")  
# Prints: Hello, my name is Oski
# f-strings allow embedding variables directly inside curly braces.

# 4. Difference between the two last print statements:
# The first uses a comma → automatically adds a space and works with multiple arguments.
# The second uses an f-string → more flexible, allows formatting, math, and expressions inside {}.

#---3.5 Terminal Commands---

#1. cd
# Changes directories. Use it to move from one folder to another.
# Example: cd Desktop

# 2. ls
# Lists files and folders in the current directory.
# Example: 
#   ls 
#   hw1_folder.png


# 3. ls -a
# Lists all files, including hidden ones (files starting with a dot).
# Example: ls -a

# 4. mkdir
# Creates a new directory (folder).
# Example: mkdir homework1

# 5. cat
# Displays the contents of a file in the terminal.
# Example: cat datatypes.py

# 6. pwd
# Prints the current working directory (shows where you are).
# Example: pwd
    #pwd
    #/c/Users/andyj/OneDrive/escritorio/python_decal_fa25/andy/homework1

# 7. cd ..
# Moves one level up in the directory tree (to the parent folder).
# Example: cd ..

# 8. cd .
# Stays in the same directory (current folder). Rarely useful alone.
# Example: cd .

# 9. cd ~
# Takes you back to your home directory.
# Example: cd ~

# 10. cp
# Copies a file or folder.
# Example: cp file.txt backup_file.txt

# 11. mv
# Moves or renames a file or folder.
# Example: mv file.txt Documents/

# 12. rm
# Deletes a file. 
# Example: rm old_file.txt

# 13. clear
# Clears the terminal screen.
# Example: clear

# 14. grep
# Searches for specific text inside files.
# Example: grep "hello" notes.txt

##QUESTIONS
#1. Look up 3 other commands not present. Define and explain how to use them on the command line.
# touch
# Creates a new empty file.
# Example: touch newfile.txt

# man
# Displays the manual page (documentation) for a command.
# Example: man ls

# head
# Shows the first 10 lines of a file by default.
# Example: head notes.txt


#2. What is the difference between ls and ls -a?
#ls shows ONLY visible files
#ls -a shows ALL files, including hidden files

#3. What is a hidden file?
#A hidden file is by default hidden to avoid cluttering dorectories with config/system files

#4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
# ls -lh
# long listing format, in human readable sizes
# Example: ls -lh

# ls -t
# sorts by modification time
# Example: ls -t

# ls -S
# Sorts by size
# Example: ls -S



