"""
Code file for branch and bound problem created for Advanced Algorithms
Spring 2020 at Olin College. These functions run tests on student 
solutions to the branch and bound implementation on integer programming
(bab_starter.py).
No need to edit this code, it has been provided for your convenience!
"""

from bab_starter import BBTreeNode
import picos as pic
from picos import RealVariable

def problem1():
    """
    Test sample problem 1.
    """
    print("Problem 1")
    fail_count = 0
    x = RealVariable("x")
    y = RealVariable("y")
    z = RealVariable("z")
    vars = [x, y, z]
    objective = z
    constraints = [z == x + y, -5*x + 4* y <= 0, 6*x+2*y <= 17, x >= 0, y >= 0]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()

    correct_vals = [2.0, 2.0, 4.0]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 1 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def problem2():
    """
    Test sample problem 2.
    """
    print("Problem 2")
    fail_count = 0
    x = RealVariable("x") 
    y = RealVariable("y") 
    z = RealVariable("z") 
    vars = [x, y, z]
    objective = z
    constraints = [x+y <= 7, 12*x+ 5*y <= 60, x >= 0, y >=0, z == 80 * x + 45 * y]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()
    
    correct_vals = [3.0, 4.0, 420]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 2 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def problem3():
    """
    Test sample problem 1.
    """
    print("Problem 3")
    fail_count = 0
    x = RealVariable("x") 
    y = RealVariable("y") 
    z = RealVariable("z") 
    vars = [x, y, z]
    objective = z
    constraints = [z == 4*x+5*y, 3*x +1 * y <= 27, 6 *x + 4*y >= 6, 5 * x + 5 * y >= 1, x >= 0, y >=0]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()
    
    correct_vals = [0.0, 27.0, 135]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 3 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def problem4():
    """
    Test sample problem 4.
    """
    print("Problem 4")
    fail_count = 0
    x = RealVariable("x") 
    y = RealVariable("y") 
    z = RealVariable("z") 
    vars = [x, y, z]
    objective = z
    constraints = [z == 3*x + 5 * y,2 * x + 4 * y <= 25, x <= 8, x>= 0, y >= 0]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()
    
    correct_vals = [8.0, 2.0, 34]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 4 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def problem5():
    """
    Test sample problem 5.
    """
    print("Problem 5")
    fail_count = 0
    x = RealVariable("x") 
    y = RealVariable("y") 
    z = RealVariable("z") 
    vars = [x, y, z]
    objective = z
    constraints = [z == 5 * x + 6 *y, x + y <= 5, 4*x+7*y <= 28, x>= 0, y >= 0]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()
    
    correct_vals = [3.0, 2.0, 27]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 5 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def problem6():
    """
    Test sample problem 6.
    """
    print("Problem 6")
    fail_count = 0
    x = RealVariable("x") 
    y = RealVariable("y") 
    z = RealVariable("z")
    a= RealVariable("a")
    b= RealVariable("b")
    c = RealVariable("c")
    vars = [x, y, a, b, c,  z]
    objective = z
    constraints = [z == 15*x + 20 *y + 18* a + 13 * b + 12* c, 18*x+10*y+21*a+11*b+11*c <= 50, x>= 0, y >= 0, a >= 0, b >= 0, c >= 0, x <= 1, y <= 1, a <= 1, b <= 1, c <= 1]
    root = BBTreeNode(constraints = constraints, objective = objective, vars = vars)
    res, sol_vars = root.bbsolve()
    
    correct_vals = [1.0, 1.0, 0.0,1.0, 1.0, 60.0]

    check_index = 0

    while check_index < len(correct_vals):
        try:
            assert(abs(correct_vals[check_index] - float(sol_vars[check_index])) < 1e-4)
        except AssertionError:
            print("Test case 6 failed on variable at index " + str(check_index))
            fail_count = 1
        check_index += 1

    return fail_count

def run_all_tests():
    """
    Runs all the sample tests for branch and bound.
    """
    fail_count = 0

    fail_count += problem1()
    fail_count += problem2()
    fail_count += problem3()
    fail_count += problem4()
    fail_count += problem5()
    fail_count += problem6()
    # Print total number of failed tests
    print("All tests completed with " + str(fail_count) + " failure(s).")

if __name__ == '__main__':
    # Runs all tests we have for the branch and bound problem
    run_all_tests()
