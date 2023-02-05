# Branch and Bound
For assignment instructions, please see [branch_and_bound_problem.pdf](./branch_and_bound_problem.pdf) .
## Setup on Ubuntu
If you're using Ubuntu, you're in luck! All you have to do is run `pip install -r requirements.txt` and you should be good to go. After that, just run `bab_test.py`. If you get the following output, you're set to start working on `bab_starter.py`:

```
Problem 1
Test case 1 failed on variable at index 1
Test case 1 failed on variable at index 2
Problem 2
Test case 2 failed on variable at index 0
Test case 2 failed on variable at index 1
Test case 2 failed on variable at index 2
Problem 3
Problem 4
Test case 4 failed on variable at index 1
Test case 4 failed on variable at index 2
Problem 5
Test case 5 failed on variable at index 0
Test case 5 failed on variable at index 1
Test case 5 failed on variable at index 2
Problem 6
Test case 6 failed on variable at index 0
Test case 6 failed on variable at index 2
Test case 6 failed on variable at index 5
All tests completed with 5 failure(s).
```

If this fails for some reason and you can't sort out the errors, use the instructions below to complete your work.

## Setup on any other OS
You're also in luck! While cvxopt - a dependency for picos, the solver we are using - does not play nice with M1 architecture (and probably doesn't play well with other systems either), I have included a file called Dockerfile that will allow you to run the code in a python3/Ubuntu Docker container and use VSCode (Atom is sunsetting, so you're going to have to make the smart decision to move to VSCode sometime anyway). I discourage using Windows - Docker and Windows do not play nice.


1. Download a version of [Docker Desktop](https://www.docker.com/products/docker-desktop/) that is compatible with your system (NOTE: you've decided to use Windows and installing the newest version doesn't work for you, try installing Docker 3.6.0)
2. Download [VSCode](https://code.visualstudio.com/download) if you don't already have it
3. In VSCode, install the Dev Containers extension
4. Click on the green >< in the bottom left corner of the window
5. Click on "Open Folder in Container" in the dropdown
6. Click "From Dockerfile" when prompted in the dropdown
7. Navigate to and open this folder (`bab`)
8. Run the following commands using the VSCode terminal:
    1. `export CPPFLAGS="-I/usr/include/suitesparse"`
    2. `pip install -r requirements.txt`

After completing these steps, you should be able to run your code in the VSCode terminal. To test it out, run `bab_test.py`. If you get the following output, you're set to start working on `bab_starter.py`:

```
Problem 1
Test case 1 failed on variable at index 1
Test case 1 failed on variable at index 2
Problem 2
Test case 2 failed on variable at index 0
Test case 2 failed on variable at index 1
Test case 2 failed on variable at index 2
Problem 3
Problem 4
Test case 4 failed on variable at index 1
Test case 4 failed on variable at index 2
Problem 5
Test case 5 failed on variable at index 0
Test case 5 failed on variable at index 1
Test case 5 failed on variable at index 2
Problem 6
Test case 6 failed on variable at index 0
Test case 6 failed on variable at index 2
Test case 6 failed on variable at index 5
All tests completed with 5 failure(s).
```

All changes you make in the container should be saved locally to the same place, so as long as you save your work, you should be fine.

Feel free to have a look at the Dockerfile to see what I did. Docker is really useful if you need to run code on another OS and is less clunky than a VM; I highly suggest looking into it! :)
