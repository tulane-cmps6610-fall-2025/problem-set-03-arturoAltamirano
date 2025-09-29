# CMPS 6610 Problem Set 03
## Answers

**Name:** Arturo Altamirano

Place all written answers from `problemset-03.md` here for easier grading.

- **1b.**

    this iterative algorithm has the following steps: 

    1. check the base case, if n is not of length 0 -----> + 1

    2. evaluate the boolean condition, is our index equivalent to our
       target for every element in the list  -----> O(n - 1)

    this can be denoted as: 

        T(n - 1) + 1

        T((n - 2) + 1) + 1 

        T(n - 3) + 3

        consider that this is essentially: 

        T(n - c) + 1 * c

        just n plus/minus some constant - if you ignore the constants as n grows increasingly large...
        
        you are left with simply: T(n)

    **Work: O(n)**

    **Span: O(n)**

    Within here is my inductive proof for these assertions. I understand these are unneccesary, but I wanted the practice after doing this incorrectly on HW1:

    <details>
    Inductive Hypothesis: In every recursive call of iterate, it will return the boolean evaluation result comparing our target to our current index. 

    Base Case: 

    (n - 1) + 1



    </details>




- **1d.**

    this divide and conquer algorithm has the following steps: 

    1. check the base case, if n is not of length 0 -----> + 1

    2. divide the input into 2 sublists, do this recursively until it is 
       no longer possible. -----> 2/n

    3. in parallel, check all of these divisions for equivalence to our 
       target value ------> 2w
    
    4. recombine these results to achieve our final output ----> n

    this can be denoted as: 

        T(n) = 2T(n/2) + n + 1

        T(n) = 2(2T(n/4) + (n/2)) + 2n

        T(n) = 4T(n/8) + 2(n/4) + 3n

    we begin to see the form: 

    2<sup>k</sup>(n/2<sup>k</sup>) + k * n

    you can set this guy to a constant at this point:

    2<sup>log 2 n</sup> T(1) + log <sub>2</sub>i * n

    this becomes equivalent to:

    n * 1 + n log<sub>2</sub> * n

    we can state that log<sub>2</sub> n dominates the constant at large growth,
         
    we can then simplify to:

    **Work: O(n)**

    **Span: O(n log n)**

- **1e.**

    This algorithm divides unevenly, and as such will have a dominant side as n grows.

    The recurrence can be taken as: 

        T(n) = T(2n/3) + T(n/3) + n + 1

        we can unwind both of these to get: 

        (2n/9 + 4n/9 + n/9) + (n/9 + n + n)

        (4n/27 + 8n/27 + 2n/3) + (n/27 + 1 + 1) 

    we can note that the left portion is beginning to dominate this process

    analyzing it's structure and root dominated growth we can see that c * n in the master case is:

    **work:  O(n)**

    **span: O(n)**

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

            T(n) = (T(n - 3) + T(n - 2) + T(n - 1) + n ^ 2)

            We can denote this as balanced as the arrays only increment/decrement by 1 at each step, but that growth is quadratic since n increases by a exponent factor for every unfolding. This is because we need to re-traverse our duplicates array at every iteration to see if the current index is a duplicate. 

            Interesting to note that, even with work being largest at the root, the factor decrease is still 'linearly constant' and not by a constant fraction, so we cannot say it is leaf dominated.

    **asymptotic notation: O(n<sup>2</sup>)**


- **3b.**

    This recursive iteration has a singular comparison and an addition operation. 

        T(n) = T(n - 1) + O(1)

        = T((n - 2) + 1) + 1

        = T(n - 3) + 1 + +1 

        this is of linear balanced growth and has the fundamental form:

        T(n - c) + (1 * c)

        the constants are dominated by the size of n, with no parralelization opportunity, and as such:

    **Work = O(n)**

    **Span = O(n)**

- **3d.**

    This recursive scan has the following steps: 

        T(n) = T(n - 1) + O(n) + 1

        T((n - 2) + (n - 1) + n +  1)

        T(n - 3) + (n - 2) + (n - 1) + n + 3

        what method to use to derive this? 

    **O(n<sup>2</sup>)**

- **3f.**

    This divide and conquer algorithm has 3 steps: 

        divide the input into halves until no longer possible -----> n/2

        evaluate equivalence to strings -----> +1

        merge all divisions and evaluations together -----> 2T

        this can be denoted as: 

        2T(n/2) + 1

        2(2T(n/4) + (n/2)) + 2

        4T(n/16) + 2(n/4) + 3

    leaf dominated, so use n <sup> log <sub>b</sub> a </sup>

    n<sup>log<sub>2</sub>2</sup> == n<sup>1</sup>

    **O(n)**





