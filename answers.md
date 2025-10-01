# CMPS 6610 Problem Set 03
## Answers

**Name:** Arturo Altamirano

Place all written answers from `problemset-03.md` here for easier grading.

- **1b.**

    this iterative algorithm has the following steps: 

    1. check the base case, ensure n is not of length 0: O(1)

    2. evaluate the boolean condition, is our index equivalent
       to our target for every element in the list: O(n - 1)

        unrolling: 

        T(n - 1) + 1

        T(n - 2) + 1 + 1 

        T(n - 3) + 3

        consider that this is essentially: 

        T(n - c) + 1 * c

        just n plus/minus some constant - if you ignore the constants as n grows increasingly large...
        
        you are left with clear linear growth

    **Work: O(n)**

    **Span: O(n)**

- **1d.**

    this divide and conquer algorithm has the following steps: 

    1. divide the input into 2 sublists, do this recursively until it is no longer possible: 2/n

    2. in parallel, check all of these divisions for equivalence to our 
       target value: 2w
    
    3. recombine these results to achieve our final output: 1

    this can be denoted as: 

        T(n) = 2T(n/2) + n 

        T(n) = 2(2T(n/4) + (n/2)) + 2n

        T(n) = 4(2T(n/8) + 2(n/4)) + 3n

    we begin to see the balanced form clearly and can specify: 

    log<sub>2</sub>2 + c * 1
         
    we can then simplify to:

    **Work: O(n)**

    **Span: O(log n)**

- **1e.**

    This algorithm divides unevenly, and as such will have a dominant side as n grows.

    The recurrence can be taken as: 

        T(n) = T(2n/3) + T(n/3) + 1

        we can unwind both of these to get: 

        (2n/9 + 4n/9 + n/9) + (n/9 + 1)

        (4n/27 + 8n/27 + 2n/3) + (n/27 + 1 + 1) 

    we can note that the left portion is beginning to dominate this process

    analyzing it's structure and root dominated growth we can see that c * n is:

    **work: O(n)**

    **span: O(log n)**

- **2a.**

    I am constructing this according to documentation in the CMU notebook: https://www.cs.cmu.edu/~rwh/isml/book.pdf

    I designed this to be recursive, as Standard ML and SPARC seem to expect all iteration in the form of recursion according to Chapter 7.2 and 9.

    I am also adapting the matching conventions outlined in 27.2 and in the regular expression package.

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

    1. Pass our list to recurseCheck and begin assigning values across the array. Assuming = [] base case passed

    2. For every element x, we compare to the remaining tail xs, we then pass to evaluator to determine our duplicates list operation

    3. If the evaluator determines according to our current index and the seen list that we have seen the current value before (y, x::xs) = (y = x) then it will return the boolean of this 

    4. Else we need to add xs to the seen list using xs::seen, updating the current x state to be the recursive call of this operation 

    This program does 3 total operations: 
        
        The evaluation stub checks if y = x according to duplicates array: O(n)

        The initial case test of our input and subsequent base tests: (n - 1)

    This can be denoted as: 

        T(n - 1) + O(n)

        with: n-1 being the size of our original list, which we are traversing and O(n) + 1 being the duplicates list which we are growing and evaluating according to size n 

        the recurrence unfolding: 

            T(n) = T(n - 2) + T(n - 1) + n

            T(n) = (T(n - 3) + T(n - 2) + T(n - 1) + n ^ 2)

        We can denote this as balanced as the arrays only increment/decrement by 1 at each step, but that growth is quadratic since n increases by a exponent factor for every unfolding. This is because we need to re-traverse our duplicates array at every iteration to see if the current index is a duplicate. 

        Interesting to note that, even with work being largest at the root, the factor decrease is still 'linearly constant' and not by a constant fraction, so we cannot say it is leaf dominated.

    **work = O(n<sup>2</sup>)**

    **span = O(n<sup>2</sup>)**

    This algorithm is quite bad and I am certain there is something better in existence. I had a great deal of difficulty trying to construct something better and apologize if this is unsatisfactory. The order preservation constraint made this difficult for me. 

- **2b.**

    Given a series of lists [[A0].....[Am]] of n unsorted elements with duplicates:

        #seperate evaluating function to be called for every recursion

        fun evaluator(y, []) = false
            | evaluator(y, x::xs) = (y = x) orelse evaluator (y , xs)

        fun recurseCheck ([], duplicate) = []
                | recurseCheck (x :: xs, duplicate) = 

                    #if we have already seen it across xs, then continue 

                    if evaluator (x , duplicate) then:
                        recurseCheck(xs , duplicate)

                    #else we set x to the recursive iteration of #recurseCheck, adding x to the seen(duplicate) list

                    else:
                        x :: recurseCheck(xs, xs::duplicate)
        
        fun recurseCheckLists ([], duplicate) = []
                | recurseCheckLists (x :: xss, duplicate) =

                let 
                    # define another recursive iteration - essentially nesting this process to a # second level of iteration among lists 
                    intermediary = recurseCheck(xs, duplicate)
                    newDuplicate = intermediary :: duplicate

                in 
                    recurseCheclLists(xss, newDuplicate)
                    
        in recurseCheck(A, [])

    1. Pass our list to recurseCheck and begin assigning values across the array. Assuming = [] base case passed

    2. For every element x, we compare to the remaining tail xs, we then pass to evaluator to determine our duplicates list operation

    3. If the evaluator determines according to our current index and the seen list that we have seen the current value before (y, x::xs) = (y = x) then it will return the boolean of this 

    4. Else we need to add xs to the seen list using xs::seen, updating the current x state to be the recursive call of this operation 

    5. We then iterate to the next list in the list of lists and continue this process within the recursive structure

    I don't believe this would change the asymptotic notation or work calculation, but would have a significant effect on the average runtime.

    **work = O(n<sup>2</sup>)**

    **span = O(n<sup>2</sup>)**

- **2c.**

    An iterative approach must be used when order is neccesary to be preserved or associativity becomes a concern. 
    
    I feel as though the nested nature of my second solution enables potential for parralell iterative approaches on all lists, with some sort of intermediary structure to store their respective orderings between them, but I cannot think of the composition of such a solution.

- **3b.**

    This recursive iteration has a singular comparison (n - 1) and an addition operation (+1)

    it can be denoted as:

        T(n) = T(n - 1) + c * 1

        = T(n - 2) + 1 + 1

        = T(n - 3) + 1 ... + 1 

        this is of linear balanced growth and has the fundamental form:

        T(n - c) + (c * 1)

        the constants are dominated by the size of n, with no parralelization opportunity, and as such:

    **Work = O(n)**

    **Span = O(n)**

- **3d.**

    This recursive scan has the following steps:

    1. maps to the boolean evaluation of an input 

    2. reduce folds the input, passes to our driving function
       and returns a singular input
       
    3. evalautes if the sequence has been fully traversed

    it can be denoted as: 

        T(n) = T(n - 1) + c * n

        T((n - 2) + (n - 1 + n) +  1)

        T(n - 3) + (n - 2) + (n - 1) + n + 3

    this can be interpreted as:

    **work = O(n<sup>2</sup>)**

    **span = O(n<sup>2</sup>)**

- **3f.**

    This divide and conquer algorithm has 3 steps: 

    divide the input into halves until no longer possible:  n/2

    evaluate equivalence to strings: +1

    merge all divisions and evaluations together: 2T

        this can be denoted as: 

        2T(n/2) + c * 1

        2(2T(n/4)) + 2

        4T(n/8) + 3

    we can see that this is leaf dominated, and takes the form: 

    2<sup>k</sup>T(n/2<sup>k</sup>) + k

    we can use the master theorem case: 
    
    n <sup> log <sub>b</sub> a </sup>

    to determine that this is of:

    n<sup>log<sub>2</sub>2</sup> == n<sup>1</sup>

    **work: O(n)**

    **span: O(log n)**