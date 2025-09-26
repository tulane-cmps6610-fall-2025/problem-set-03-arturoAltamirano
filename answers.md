# CMPS 6610 Problem Set 03
## Answers

**Name:** Arturo Altamirano


Place all written answers from `problemset-03.md` here for easier grading.




- **1b.**

    Work: O(n)

    Span: O(n)


- **1d.**

    Work: O(n)

    Span: O(log n)


- **1e.**

    


- **2a.**

    I am constructing this according to documentation in the CMU notebook: https://www.cs.cmu.edu/~rwh/isml/book.pdf

    I designed this to be recursive, as Standard ML seems to encourage iteration in the form of recursion according to Chapter 7.2 and 9.

    I am also adapting the matching conventions outlined in 27.2 and in the regular expression package

    Given [list A] of n unsorted elements with duplicates:

        #seperate evaluating function to be called for every recursion

        fun evaluator(y, []) = false
            | evaluator(y, x::xs) = (y = x) orelse evaluator (y , xs)
        
        let 
            fun recurseCheck ([], duplicate) = []
                | recurseCheck (x :: xs, duplicate) = 

                    #if we have already seen it across xs, then continue 

                    if evaluator (x , duplicate) then:
                        recurseCheck(xs , duplicate)

                    #else we set x to the recursive iteration of #recurseCheck, adding x to the seen(duplicate) list

                    else:
                        x :: recurseCheck(xs, xs::duplicate)
        
        in recurseCheck(A, [])

    Basic outline: 

    1. Pass our list to recurseCheck and begin assigning values across 
       the array. Assuming = [] base case passed

    2. For every element x, we compare to the remaining tail xs, we then
       pass to evaluator to determine our duplicates list operation

    3. If the evaluator determines according to our current index and the 
       seen list that we have seen the current value before (y, x::xs) = (y = x) then it will return the boolean of this 

    4. Else we need to add xs to the seen list using xs::seen, updating the current x state to be the recursive call of this operation 

- **3b.**

    This program does 



- **3d.**





- **3f.**




- **4a.**




- **4b.**





- **4c.**




