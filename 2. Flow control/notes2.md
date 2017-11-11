# Boolean Values
- The *Boolean* data type has only two values: *True* and *False*
- They always start with a capital T or F, with the rest of the word in lowercase.

# Comparison Operators 
- == Equal to

- != Not equal to

- < Less than

- \> Greater than

- <= Less than or equal to

- \>= Greater than or equal to

The == operator (equal to) asks whether two values are the same as each other.

The = operator (assignment) puts the value on the right into the variable on the left.

# Boolean Operators
- The three Boolean operators **(and, or, and not)** are used to compare Boolean values. 

- The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.

- On the other hand, the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.

 - The not operator operates on only one Boolean value
 - *Example : not true = false, not false = true*

 # If Statement 
 - In Python, an *if* statement consists of the following:
 - *The if keyword*
 - *A condition (an expression that evaluates to True or False)*
 - *A colon*
 - *Starting on the next line*

 # Else Statement
 - An else statement doesn't have a condition. Contains the following: 
 - *The else keyword* 
 - *A colon*
 - *Starting on next line*

 **EXAMPLE** : 
 - name = 'Bob'
- if name == 'Alice':
-    print('Hi, Alice.')
- else:
-    print('Hello, stranger.')

# Elif Statements
- The elif statement is an “else if” statement that always follows an if or another elif statement. It provides another condition that is checked only if all of the previous conditions were False. 

- *The elif keyword*
- *A condition (that is, an expression that evaluates to True or False)*
- *A colon*
- *Starting on the next line, an indented block of code (called the elif clause)*

**EXAMPLE** :
- name = 'Bob'
- age = 5
- if name == 'Alice':
-    print('Hi, Alice.')
- elif age < 12:
-    print('You are not Alice, kiddo.')

# While Loop Statements
- You can make a block of code execute over and over again with a while statement. The code in a while clause will be executed as long as the while statement’s condition is True. In code, a while statement always consists of the following:

- The while keyword

- A condition (that is, an expression that evaluates to True or False)

- A colon

- Starting on the next line, an indented block of code (called the while clause)

- The code with the *if* statement checks the condition, and it prints Hello, world. only once if that condition is true. The code with the *while* loop, on the other hand, will print it five times.

# Break Statements
- If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

# Continue Statements
- Continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.

**If you ever run a program that has a bug causing it to get stuck in an infinite loop, press CTRL-C. This will send a KeyboardInterrupt error to your program and cause it to stop immediately**

# for Loops and the range() Function
- In code, a for statement looks something like for i in range(5): and always includes the following:

- The for keyword

- A variable name

- The in keyword

- A call to the range() method with up to three integers passed to it

- A colon

- Starting on the next line, an indented block of code (called the for clause)

Some functions can be called with multiple arguments separated by a comma, and range() is one of them.

# Importing Modules
- Before you can use the functions in a module, you must import the module with an import statement. In code, an import statement consists of the following:

- The import keyword

- The name of the module

- Optionally, more module names, as long as they are separated by commas

- The random.randint() function call evaluates to a random integer value between the two integers that you pass it. Since randint() is in the random module, you must first type random. in front of the function name to tell Python to look for this function inside the random module.

Here’s an example of an import statement that imports four different modules:

*import random, sys, os, math*

# Ending a Program Early with **sys.exit()**

- Since this function is in the sys module, you have to import sys before your program can use it.
