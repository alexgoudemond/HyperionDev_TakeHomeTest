<!--
Author: Alexander Goudemond
Github: https://github.com/alexgoudemond/HyperionDev_TakeHomeTest/tree/main/Section A

Date Created: 2021/01/18
-->

# HyperionDev_TakeHomeTest_SectionA

This folder contains the code review for the Take-Home Test provided by HyperionDev. It will mimick the feedback I would give to a student, having being given their code.

The coding language chosen for this code challenge is Java, as it was Option 2 in the Take-Home Test. The instructions for this task were as follows:

    In a file called recursion.java, create:
        - recursive function that reverses a string
        - a recursive function that, given a number n, prints out the first n Fibonacci numbers (Fibonacci numbers are a sequence where each number is the sum of the previous two - 0 1 1 2 3 5 8...)

The initial code provided for this code review has been saved in Section A, with a name 'recursion.java'. There are 48 lines in this code, and the rest of the sections of this README document will detail the constructive feedback I would give the student

---

# Code Review for Option 2

A quick and efficient way to make sense of a new program, especially in Object Orientated Programming (OOP), is to generate a UML diagram. For our own understanding, I have adapted a UML diagram, to show us useful and important information. Please note that the format and layout of this UML diagram is not formally correct, but for the purpose of this discussion, it conveys the important ideas.

| recursion                                    |
|----------------------------------------------|
|                                              |
| + main( args : String [] ) : void            |
| + reverse_string( myStr : String ) : String  |
| + function( maxNumber : T ) : void           |

We can see from that diagram that there are no class variables. We can also see the 3 functions we are working with, all which lie inside the class called "recursion.java"

---

Before attempting to go into the code in more detail, we can immediately see a few things we can address. 

Firstly, classes in Java should begin with a capital letter. This format assists the compiler to seperate classes from methods, as well as helps the programmer quickly understand some of the content. For example, 'HyperionDev' would be a class, 'hyperionDev' may be a variable and 'hyperionDev()' a function.

Also, the style of opening and closing braces is not consistent. There are different ways to structure our code, to improve readability, and some common examples are shown here:

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

Notice how each example uses the position of the opening and closing braces differently. Most of the provided code follows example 1, however some aspects of it change to example 2 and example 3 - making reading the code more difficult. It is recommended to stay with a single brace-style.

I have created a new java file, called 'RecursionRevised.java', which will contain these changes. The brace-style shown in Example 2 will be used in this program.

---

We are now in a position where we can look at the code in more detail!

---

After quickly skimming over the code, paying attention to the indentation, we notice that lines 21 and 22 contain a whitespace indent, as apposed to the tabspace indent used elsewhere.

We also see that the for-loop used on lines 36 - 44 is de-dented. It is wise to indent this, so that it is visibly inside/contained in the method called 'function'.

Just like the brace-style, these 2 suggestions will not affect the functionality of the code. They simply improve the code readability for the programmer.

'RecursionRevised.java' will contain these small changes as well.

---

Let us now look at the functions!

---

## reverse_string( myStr : String) : String

This method name is well described. The name of the method reveals the purpose of the function, and immediately lets us know what is trying to be achieved, well done!

We can see that lines 20 - 23 contain the base case for the recursive call, however a comment above this would help the programmer better understand the method structure. Line 24 has a useful comment on the recursive call of the function, which is great!

Now, line 26 should be our recursive call, however we can spot a Typo:

```
26      return reverseString(myStr.substring(1)) + myStr.charAt(0);}
```

The typo is the function name. we should call 'reverse_string()', as the compiler thinks that 'reverseString()' is a different method.

'RecursionRevised.java' will contain the comment and fix the typo.

---

## function( maxNumber : T ) : <T> void

This method name is not well described. It is not clear what the purpose of the function is, and so a better name is recommended. Perhaps 'fibonacci()'?

Also, although an effort is being made to use a Generic Type here, with the '< >' symbols - we only desire to calculate fibonacci with integer values. So I would propose modifying this to handle Integers only.

Then, line 30 overwrites the local variable 'maxNumber' (the variable that is also passed as a parameter). Is it possible that this was meant to be a default value? In other words, was the desire to have the code look like this:

```
28      public static <T> void function(T maxNumber) {
29          // Set it to the number of elements you want in the Fibonacci Series
30          if (maxNumber < 1) { maxNumber = 10; } //default value?
31          int previousNumber = 0;
32          int nextNumber = 1;
```

We can then see that the for loop on lines 36 - 44 is responsible for the calculation of the fibonacci numbers. However, the function we were meant to design is meant to use recursion - not a loop! For now, let us leave it in the loop, and see what the output is when we run the code later.

Also, our for loop uses a _pre-increment_ condition, instead of the usual _post-increment_ condition. A pre_increment condition is written as "++i", whereas a post_increment condition is written as "i++". I encourage you to find out: **what is the difference**?

---

## main( args : String [] ) : void

Your main function is simple and quick to read! You have a test String on line 6, which is a reversed sentence.

On line 10 you call reverse_string(), and on line 11 you print the value of 'reversed'.

On line 10, you also print a String showing the first 10 fibonacci numbers. This is hard coded... In other words, the main method does not call the method responsible for calculating the fibonnaci sequence, at all!

I would recommend replacing this String with a method call to your fibonacci function. One possible solution is the following:

```
9      //create Method and pass and input parameter string 
10      String reversed = reverse_string(myStr);
11      System.out.println("The reversed string is: " + reversed); fibonacci(10);
```

---

# Running the code

Unfortunately, due to the typo in reverse_string() (line 26) as well as the duplicate value of maxNumber in function() (line 30) and the variable parameter in function() (line 28), 'recursion.java' does not compile.

However, if we choose to run the modified code 'RecursionRevised.java', the following output is seen:

```
String to be passed in Recursive Function: mosewA si avaJ
String to be passed in Recursive Function: osewA si avaJ
String to be passed in Recursive Function: sewA si avaJ
String to be passed in Recursive Function: ewA si avaJ
String to be passed in Recursive Function: wA si avaJ
String to be passed in Recursive Function: A si avaJ
String to be passed in Recursive Function:  si avaJ
String to be passed in Recursive Function: si avaJ
String to be passed in Recursive Function: i avaJ
String to be passed in Recursive Function:  avaJ
String to be passed in Recursive Function: avaJ
String to be passed in Recursive Function: vaJ
String to be passed in Recursive Function: aJ
String to be passed in Recursive Function: J
String to be passed in Recursive Function:
String in now Empty
The reversed string is: Java is Awesome
Fibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34
```

---

# Next Steps

What I would recommend to make this code even better, is to review the proposed corrections (which are summarised below) and then identify if the code is working as expected. The code output shown above could assist with this.

In addition to this, I would like you to consider the following:
- What should happen if I pass an empty string into reverse_string()?
- What should happen if I pass a negative number into function()?
- What is the difference between a _pre-incremement_ and a _post-increment_?
- How can the code be modified so that the user can specify the string to be reversed, as well as specify the first 'n' times the Fibonacci series runs?

---

# List of proposed corrections to recursion.java

Kindly note that all of these proposed solutions have been implemented in a seperate file called 'RecursionRevised.java'. However, it is encouraged that the author generate a new file, to aid the learning process.

    1.) The class name should be 'Recursion', instead of 'recursion'
    2.) For readability, the brace-style needs to consistent
    3.) For readability, the indentation needs to be consistent
    4.) For readability, loops should be visibly indented inside functions
    5.) Should comments be placed in reverse_string()?
    6.) Should function() have a meaningful method name?
    7.) Should function() take an Integer as a parameter?
    8.) function() should be recursive, not iterative!
    9.) main() should call the fibonacci function!

---

# Overall Feedback

**Correctness** - This code aimed to reverse a string, and calculate the first 'n' fibonacci numbers in a sequence. Because the fibonacci function was not called in the main() method, and uses iteration instead of recursion, this code is not complete. If the proposed corrections were implemented, I believe this code could be completely correct.

**Efficiency** - This code is efficient, however recursion is generally slower that iteration.

**Style** - The code provided did not have a consistent indentation-style, nor did it have a consistent brace-style. Fixing these would make the code more readible.

**Documentation** - The code could benefit from some more comments and test cases.

Overall, the code is a fantastic attempt! We only needed to modify a few small things, to get it to run! 
