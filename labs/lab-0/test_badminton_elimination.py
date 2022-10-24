'''Test file for badminton elimination lab created for Advanced Algorithms
Spring 2021 at Olin College.'''

from badminton_elimination import Division


def assert_eliminated(division, team):
    '''Asserts that the team in the given division is eliminated using both
    the linear programming and the network flows methodology for solving.
    Prints a failure message if they are not.
    '''
    try:
        assert division.is_eliminated(team.ID, "Linear Programming") == True
    except AssertionError:
        print("Failure in linear programming is eliminated: " + team.name + " should be eliminated.")
    try:
        assert division.is_eliminated(team.ID, "Network Flows") == True
    except AssertionError:
        print("Failure in network flows is eliminated: " + team.name + " should be eliminated.")

def assert_not_eliminated(division, team):
    '''Asserts that the team in the given division is not eliminated using both
    the linear programming and the network flows methodology for solving.
    Prints a failure message if the program returns that they are.
    '''
    try:
        assert division.is_eliminated(team.ID, "Linear Programming") == False
    except AssertionError:
        print("Failure in linear programming is eliminated: " + team.name + " should NOT be eliminated.")
    try:
        assert division.is_eliminated(team.ID, "Network Flows") == False
    except AssertionError:
        print("Failure in network flows is eliminated: " + team.name + " should NOT be eliminated.")

def test_teams2():
    '''Runs all test cases on the input matrix that can be found in teams2.txt.
    '''
    division = Division("teams2.txt")
    for (ID, team) in division.teams.items():
        if team.name == "NewYork" or team.name == "Baltimore" or team.name == "Boston" or team.name == "Toronto":
            assert_not_eliminated(division, team)
        elif team.name == "Detroit":
            assert_eliminated(division, team)
    print("test_teams2 completed")

def test_teams4():
    '''Runs all test cases on the input matrix that was given in the lab
    description. It is stored in teams4.txt.
    '''
    division = Division("teams4.txt")
    for (ID, team) in division.teams.items():
        if team.name == "Shashank" or team.name == "Shirin":
            assert_eliminated(division, team)
        elif team.name == "Audrey" or team.name == "Jack":
            assert_not_eliminated(division, team)
    print("test_teams4 completed")

def test_teams7():
    '''Runs all test cases on the input matrix that was given in the lab
    description. It is stored in teams7.txt.
    '''
    division = Division("teams7.txt")
    for (ID, team) in division.teams.items():
        if team.name == "Ireland" or team.name == "China":
            assert_eliminated(division, team)
        elif (team.name == "U.S.A." or team.name == "England" or team.name == "France"
            or team.name == "Germany" or team.name == "Belgium"):
            assert_not_eliminated(division, team)
    print("test_teams7 completed")

def test_teams24():
    '''Runs all test cases on the input matrix that was given in the lab
    description. It is stored in teams24.txt.
    '''
    division = Division("teams24.txt")
    for (ID, team) in division.teams.items():
        if (team.name == "Team4" or team.name == "Team5" or team.name == "Team7"
            or team.name == "Team9" or team.name == "Team11" or team.name == "Team12" or team.name == "Team13"
            or team.name == "Team16" or team.name == "Team19" or team.name == "Team23"):
            assert_eliminated(division, team)
        elif (team.name == "Team0" or team.name == "Team1" or team.name == "Team2"
            or team.name == "Team3" or team.name == "Team6" or team.name == "Team8"
            or team.name == "Team10" or team.name == "Team14"
            or team.name == "Team15" or team.name == "Team16" or team.name == "Team17"
            or team.name == "Team18" or team.name == "Team20" or team.name == "Team21"
            or team.name == "Team22"):
            assert_not_eliminated(division, team)
    print("test_teams24 completed")

if __name__ == '__main__':
    test_teams2()
    test_teams4()
    test_teams7()
    test_teams24()
    print("All tests have completed.")
