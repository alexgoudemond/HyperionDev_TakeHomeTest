<!--
Author: Alexander Goudemond
Github: https://github.com/alexgoudemond/HyperionDev_TakeHomeTest/tree/main/Section A

Date Created: 2021/01/18
-->

# HyperionDev_TakeHomeTest_SectionA

This folder contains the code review for the Take Home Test provided by HyperionDev. It will mimick the feedback I would give to a student, having being given their code.

The coding language chosen for this code challenge is Java, as it was Option 2 in the Take-Home Test. The instructions for this task were as follows:

    In a file called recursion.java, create:
        - recursive function that reverses a string
        - a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...)

The initial code provided for this code review has been saved in Section A, with a name recursion.java. There are 48 lines in this code, and the rest of the sections of thisd README document will detail the constructive feedback I would give the student

---

# Code Review for Option 2

A quick and efficient way to make sense of a new program, especially in Object Orientated Programming (OOP), is to generate a UML diagram. For our own understanding, I have adapted a UML diagram, to show us useful and important information. Please note that the format and layout of this UML diagram is not formally correct, but for the purpose of this discussion, it conveys the important ideas.

| recursion                                    |
|----------------------------------------------|
|                                              |
| + main( args : String [] ) : void            |
| + reverse_string( myStr : String ) : String  |
| + function( maxNumber : T ) : void           |

We can see from that function that there are no class variables. We can also see the 3 functions we are working with, all which lie inside the class called "recursion.java"

---

Before attempting to go into the code in more detail, we can immediately see a few things we can address. 

Firstly, classes in Java should begin with a capital letter. This format assists the compiler to seperate classes from methods, as well as helps the programmer quickly understand some of the content. For example, 'HyperionDev' would be a class, 'hyperionDev' may be a variable and 'hyperionDev()' a function.

Then, although the use of indentation is mostly consistent (lines 21 and 22 are whitespaces, instead of tabspaces), the style of opening and closing braces is not. There are different ways to structure our code, to improve readability, and some common examples are shown here:

Example 1:
```
public static void main(String [] args){
    // code goes here
    // ...
}
```

Example 2:
```
public static void main(String [] args)
{
    // code goes here
    // ...
}
```

Example 3:
```
public static void main(String [] args){
    // code goes here
    // ... }
```

Notice how each example uses the position of the opening and closing braces differently. Most of your code follows example 1, however some aspects of it change to example 2 and example 3 - making reading the code more difficult. It is recommended to stay with a single brace-style, and with this code review - Example 2 will be used.

I have created a new java file, called 'RecursionRevised.java', which will contain these changes.

We are now in a position where we can look at the code in more detail!

---

The next thing that I would like to do is to skim over the code, trying to get an idea of what it looks like. By quickly skimming over the code, paying attention to the indentation, we notice that lines 21 and 22 contain a whitespace indent, as apposed to the tabspace indent used elsewhere.

We also see that the for-loop used on lines 36 - 44 is de-dented. It is wise to indent this, so that it is visibly inside/contained in the method called 'function'.

Just like the brace-style, these 2 suggestions will not affect the functionality of the code. They simply improve the code readability for the programmer.

'RecursionRevised.java' will contain these small changes as well.

---

# List of proposed corrections to recursion.java

    1.) The class name should be 'Recursion', instead of 'recursion'
    2.) The brace-style needs to consistent
    3.) The indentation needs to be consistent
    4.) Loops should be visibly indented inside functions
