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

    4. Else we need to add xs to the seen list using xs::seen, updating 
       the current x state to be the recursive call of this operation 

- **2c.**

    This program does 3 total operations: 
        
        The evaluation stub checks if y = x according to duplicates array  -----> O(n)

        The initial case test of our input and subsequent base tests -----> (n - 1)

        The recursive call and associated index adjustment -----> ... + 1

    This can be denoted as: 

        T(n-1) + O(n) + 1

        with: n-1 being the size of our original list, which we are traversing and O(n) + 1 being the duplicates list which we are growing and evaluating according to size n 

        the recurrence unfolding: 

        T(n) = (T(n - 2) + T(n - 1) + n) + 1

        T(n) = (T(n - 3) + T(n - 2) + T(n - 1) + n<sup>2</sup>)

        We can denote this as balanced as the arrays only increment/decrement by 1 at each step, but that growth is quadratic since n increases by a exponent factor for every iteration. 

        Interesting to note that, even with work being largest at the root, the factor decrease is still 'linearly constant' and not by a constant fraction, so we cannot say it is leaf dominated.

        O(n<sup>2</sup>)


- **3b.**


- **3d.**





- **3f.**




- **4a.**




- **4b.**





- **4c.**




