# Lab 0: Badminton Elimination 
The full lab description can be found [here](/Lab_0.pdf).

**Implement the network flows and the linear programming approach to the problem in
Python (we are providing input files and starter code).**

Use `pip install -r requirements.txt` to install the requirements for the
right libraries (you might want to use pip3 to use python3).

We have also provided a test file (`test_badminton_elimination.py`).
At a minimum, your code should pass all of the tests in that file.

Feel free to add your own additional test cases if you would like to more robustly
test your code. If you think the test cases we have given you are sufficient, please
explain how either in a comment or in your answer to this question. We aren't evaluating
you on this test cases portion, but it's a good exercise to go through. To run your code
on a specific input table (defined in a txt file, see `teams2.txt` and `teams4.txt` for examples),
you can simply run `python badminton_elimination.py teams2.txt`

We recommend using the `networkx` function to solve the problem using network flows
(documentation can be found [here](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.flow.maximum_flow.html))
and using the `picos` solver to solve the problem using linear programming
(documentation can be found [here](https://picos-api.gitlab.io/picos/graphs.html#max-flow-min-cut-lp)).

Your program should be able to answer the following question:
Who is eliminated given a table of the current standings? You should be able to
do this using a network flows approach and a linear programming approach.

Example input (the 4 at the top represents the \# of teams in the division and the
remainder of the rows and columns correspond to the same rows and columns as were
specified in the table in part 1):
```
4
Gati      83 71  8  0 1 6 1
Sam       80 79  3  1 0 0 2
Zoe       78 78  6  6 0 0 0
Lilo      77 82  3  1 2 0 0

Corresponding output:
Gati: Eliminated? False
Sam: Eliminated? True
Zoe: Eliminated? False
Lilo: Eliminated? True
```
