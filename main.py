#problem-set-03

# no other imports needed
from collections import defaultdict
import math
#

### PART 1: SEARCHING UNSORTED LISTS

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

# search an unordered list L for a key x using iterate
def isearch(L, x):
    #use this lambda with boolean or to build a list of True/False results for our calls to our function
    #this will act as an accumulator for 
    return iterate(lambda a, b: a or b, False, [e == x for e in L])

def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert isearch([], 2) == (2 in [1, 3, 5])

test_isearch()

def reduce(f, id_, a):
    print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

# search an unordered list L for a key x using reduce
def rsearch(L, x):
    return reduce(lambda a, b: a or b, False, [e == x for e in L])

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 7) == (7 in [1, 3, 5, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])
    assert rsearch([], 2) == (2 in [1, 3, 5])

test_rsearch()

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(reduce(f, id_, a[:len(a)//3]),
                 reduce(f, id_, a[len(a)//3:]))


### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """

    return iterate(parens_update, 0, mylist) == 0


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """

    if current_output < 0:
      return current_output
    
    else:
      if next_input == '(':
        return current_output + 1
    
      elif next_input == ')':
        return current_output - 1
    
      else:
        return current_output


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative([]) == True

test_parens_match_iterative()


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    mapped = list(map(paren_map, mylist))
    prefixes, total = scan(lambda a, b: a + b, 0, mapped)
    return total == 0 and(len(prefixes) == 0 or min(prefixes) >= 0)

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False
    assert parens_match_scan([]) == True

test_parens_match_scan()

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###
    # base cases
    
    # recursive case
    # - first solve subproblems
    
    # - then compute the solution (R,L) using these solutions, in constant time.

    if len(mylist) == 0:
        return (0, 0)
    
    elif len(mylist) == 1:

        if mylist[0] == '(':
            return (0, 1)
        
        elif mylist[0] == ')':
            return (1, 0)
        
        else:
            return (0, 0)
    
    # divide
    mid = len(mylist) // 2
    r1, l1 = parens_match_dc_helper(mylist[:mid])
    r2, l2 = parens_match_dc_helper(mylist[mid:])
    
    # conquer (merge)
    match = min(l1, r2)
    r_total = r1 + (r2 - match)
    l_total = l2 + (l1 - match)
    
    return (r_total, l_total)
    ###
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True 

test_parens_match_dc()