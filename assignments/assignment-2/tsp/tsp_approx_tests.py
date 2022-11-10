"""
Advanced Algorithms HW2 Testing Functions for tsp_approx_starter.py
"""

import math

##############################################################################
# The following functions generate test maps to run the algorithm on!


def getMap(mapNum=0):
    """
    Returns the adjacency matrix and city names for the map.

    Args:
        mapNum (int): the number of which map to select.

    Returns:
        adjMat (list of lists of ints): the adjacency matrix.
        cityList (list of strs): the list of the cities.
        optTour (str): string of the optimal tour.
        optList (list of ints): array of the optimal tour (each city
            is denoted by their rank: their numbering in cityList).
    """
    if mapNum == 0:
        cityList = ['a', 'b', 'c', 'd']
        adjMat = [[0, 2, 8, 5], [2, 0, 7, 4], [8, 7, 0, 6], [5, 4, 6, 0]]
        optTour = '\nOptimal Tour:' + '\na\nb\nc\nd\na\n\nWeight of Optimal Tour:\n20'
        optList = [0, 1, 2, 3, 0]
        return adjMat, cityList, optTour, optList

    elif mapNum == 1:
        cityList = ['a', 'b', 'c', 'd']
        adjMat = [[0, 2, 2, 3], [2, 0, 3, 2], [2, 3, 0, 2], [3, 2, 2, 0]]
        optTour = '\nOptimal Tour:' + '\na\nb\nd\nc\na\n\nWeight of Optimal Tour:\n8'
        optList = [0, 1, 3, 2, 0]
        return adjMat, cityList, optTour, optList

    elif mapNum == 2:
        cityList = [
            'NYC',
            'Urbandale',
            'Chicago',
            'Durham',
            'LA',
            'Seattle',
            'Washington DC',
        ]
        lats = [40.71, 41.63, 41.88, 35.99, 34.05, 47.61, 38.91]
        longs = [74.01, 93.71, 87.63, 78.90, 118.24, 122.33, 77.04]
        optTour = (
            '\nOptimal Tour:\nNYC\nChicago\nUrbandale\nSeattle\nLA'
            + '\nDurham\nWashington DC\nNYC\n\nWeight of Optimal '
            + 'Tour:\n9796'
        )
        optList = [0, 2, 1, 5, 4, 3, 6, 0]

    elif mapNum == 3:
        cityList = [
            'London',
            'Paris',
            'Madrid',
            'Rome',
            'Berlin',
            'Istanbul',
            'Moscow',
            'Athens',
            'Copenhagen',
        ]
        lats = [51.51, 48.86, 40.42, 41.90, 52.52, 41.01, 55.76, 37.98, 55.68]
        longs = [0.13, -2.35, 3.70, -12.50, -13.41, -28.98, -37.62, -23.73, -12.57]
        optTour = (
            '\nOptimal Tour:\nLondon\nBerlin\nCopenhagen\nMoscow\n'
            + 'Istanbul\nAthens\nRome\nMadrid\nParis\nLondon\n\nWeight '
            + 'of Optimal Tour:\n8978'
        )
        optList = [0, 4, 8, 6, 5, 7, 3, 2, 1, 0]

    elif mapNum == 4:
        cityList = [
            'NYC',
            'Urbandale',
            'Chicago',
            'Durham',
            'LA',
            'Seattle',
            'Washington DC',
            'Houston',
            'Phoenix',
            'Denver',
            'San Francisco',
            'Honolulu',
            'Boston',
            'Cleveland',
        ]
        lats = [
            40.71,
            41.63,
            41.88,
            35.99,
            34.05,
            47.61,
            38.91,
            29.76,
            33.45,
            39.74,
            37.77,
            21.31,
            42.36,
            41.50,
        ]
        longs = [
            74.01,
            93.71,
            87.63,
            78.90,
            118.24,
            122.33,
            77.04,
            95.37,
            112.07,
            104.99,
            122.42,
            157.86,
            71.06,
            81.69,
        ]
        optTour = '\nOptimal Tour: ?'
        optList = []

    elif mapNum == 5:
        cityList = [
            'London',
            'Paris',
            'Madrid',
            'Rome',
            'Berlin',
            'Istanbul',
            'Moscow',
            'Athens',
            'Copenhagen',
            'Dublin',
            'Warsaw',
            'Kiev',
        ]
        lats = [
            51.51,
            48.86,
            40.42,
            41.90,
            52.52,
            41.01,
            55.76,
            37.98,
            55.68,
            53.35,
            52.23,
            50.45,
        ]

        longs = [
            0.13,
            -2.35,
            3.70,
            -12.50,
            -13.41,
            -28.98,
            -37.62,
            -23.73,
            -12.57,
            6.26,
            -21.01,
            -30.52,
        ]
        optTour = (
            '\nOptimal Tour:\nLondon\nParis\nMadrid\nRome\nAthens\n'
            + 'Istanbul\nKiev\nMoscow\nWarsaw\nBerlin\nCopenhagen\n'
            + 'Dublin\nLondon\n\nWeight of Optimal Tour:\n9911'
        )
        optList = []

    elif mapNum == 6:
        cityList = [
            'London',
            'Paris',
            'Madrid',
            'Rome',
            'Berlin',
            'Istanbul',
            'Moscow',
            'Athens',
            'Copenhagen',
            'Dublin',
            'Warsaw',
            'Kiev',
            'St. Petersburg',
            'Stockholm',
        ]
        lats = [
            51.51,
            48.86,
            40.42,
            41.90,
            52.52,
            41.01,
            55.76,
            37.98,
            55.68,
            53.35,
            52.23,
            50.45,
            59.93,
            59.33,
        ]
        longs = [
            0.13,
            -2.35,
            3.70,
            -12.50,
            -13.41,
            -28.98,
            -37.62,
            -23.73,
            -12.57,
            6.26,
            -21.01,
            -30.52,
            -30.34,
            -18.07,
        ]
        optTour = '\nOptimal Tour: ?'
        optList = []

    elif mapNum == 7:
        N = 75
        cityList = []
        lats = []
        longs = []
        lab = 0
        for ind in range(0, N + 1):
            cityList.append(str(lab))
            lats.append(ind * 180 / N - 90)
            longs.append(-10)
            lab += 1
        for ind in range(1, N - 1):
            cityList.append(str(lab))
            lats.append(90 - ind * 180 / N)
            longs.append(170)
            lab += 1
        antiPolar = -(lats[0] + lats[-1]) / 2
        lats.append(antiPolar)
        longs.append(-10)
        cityList.append(str(lab))
        optTour = '\nOptimal Tour: 40030.173592'
        optList = []

    elif mapNum == 8:
        N = 75
        cityList = []
        lats = []
        longs = []
        lab = 0
        for ind in range(0, N + 1):
            cityList.append(str(lab))
            lats.append(ind * 180 / N - 90)
            longs.append(-10)
            lab += 1
        for ind in range(1, N - 1):
            cityList.append(str(lab))
            lats.append(90 - ind * 180 / N)
            longs.append(170)
            lab += 1
        antiPolar = -(lats[0] + lats[-1]) / 2
        lats.insert(0, antiPolar)
        longs.insert(0, -10)
        cityList.insert(0, str(lab))
        optTour = '\nOptimal Tour: 40030.173592'
        optList = []

    else:
        raise Exception('Not a valid map number.')

    # Get the distances and insert into the adjacency matrix.
    adjMat = [[0 for x in range(0, len(cityList))] for x in range(0, len(cityList))]
    for r in range(0, len(adjMat)):
        for c in range(r + 1, len(adjMat[r])):
            adjMat[r][c] = getDist(lats[r], longs[r], lats[c], longs[c])
            adjMat[c][r] = adjMat[r][c]
        adjMat[r][r] = 0

    return adjMat, cityList, optTour, optList


##############################################################################


def getDist(lat1, long1, lat2, long2):
    """
    Takes in two coordinates and returns the distance between them
    (in km).

    Args:
        lat1 (float): the latitude of the first city.
        long1 (float): the longitude of the first city.
        lat2 (float): the latitude of the second city.
        long2 (float): the longitude of the second city.

    Returns:
        dist (int): the distance between the two cities (km).
    """
    # Convert to radians.
    lat1 = lat1 * math.pi / 180
    long1 = long1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    long2 = long2 * math.pi / 180

    # Calculate the change in lat and long.
    dLat = lat2 - lat1
    dLong = long2 - long1

    # Set the radius of the Earth.
    R = 6371  # km

    # Calculate the distance using the formula for distance on a great circle.
    a = math.sin(dLat / 2) ** 2 + (
        math.cos(lat1) * math.cos(lat2) * math.sin(dLong / 2) ** 2
    )
    if abs(a) < 1e-15:
        a = 0
    if abs(1 - a) < 1e-15:
        a = 1
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = R * c
    return dist  # km


##############################################################################


def testMSTApprox():
    """
    Tests your code on the various maps.

    Returns:
        s (str): a string indicating number of tests passed.
    """
    Mpass = 0
    Tpass = 0
    Mflag = False
    Tflag = False
    t = 9
    tol = 1e-6

    # Test MST approximation of Metric TSP.
    MSTws = [
        12,
        6,
        5999.977279,
        6909.105275,
        11810.893206,
        7724.194671,
        8813.919553,
        39763.305768,
        39763.305768,
    ]
    for ind in range(0, t):
        MSTw = MSTws[ind]
        m = Map(ind)
        m.getMST()
        if len(m.mst) < len(m.cities) - 1:
            print('Test %d: Not enough edges in MST.' % ind)
            Mflag = True
        if len(m.mst) > len(m.cities) - 1:
            print('Test %d: Too many edges in MST.' % ind)
            Mflag = True
        w = 0
        for e in m.mst:
            w += e.weight
        if w < MSTw - tol:
            print('Test %d: MST weight too low.' % ind)
            Mflag = True
        if w > MSTw + tol:
            print('Test %d: MST weight too high.' % ind)
            Mflag = True
        if not Mflag:
            m.getTSPApprox()
            w = 0
            if len(m.tour) > 0:
                for r in range(0, len(m.tour) - 1):
                    w += m.adjMat[m.tour[r]][m.tour[r + 1]]
            else:
                w = math.inf
            if len(m.tour) != len(m.cities) + 1:
                print('Test %d: TSP should be length %d.' % (ind, len(m.cities) + 1))
                Tflag = True
            if w == math.inf:
                print('Test %d: No TSP reported.' % ind)
                Tflag = True
            else:
                if w > 2 * MSTw + 2 * tol:
                    print('Test %d: TSP too large.' % ind)
                    Tflag = True
                if w <= MSTw - tol:
                    print('Test %d: TSP too small.' % ind)
                    Tflag = True
            if m.tour[0] != m.tour[-1]:
                print('Test %d: TSP start != end.' % ind)
                Tflag = True
            for c in range(1, len(m.tour)):
                city = m.tour[c]
                if city in m.tour[c + 1 :]:
                    print('Test %d: Repeated City in TSP.' % ind)
                    Tflag = True
            if ind == 7:
                ans = 40030.173592
                ans2 = 78992.875888
                if (w < ans - tol) or (w > ans + tol):
                    print(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from left to right)!'
                        % ind
                    )
                    flag_left = True
                if (w < ans2 - tol) or (w > ans2 + tol):
                    print(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from right to left)!'
                        % ind
                    )
                    flag_right = True
                if flag_left and flag_right:
                    print(
                        "[FAILED} Test %d: Wrong TSP considering both directions of DFS traversal"
                        % ind
                    )
                    Tflag = True
                if (flag_left or flag_right) and not Tflag:
                    print("Test %d still passed." % ind)
            if ind == 8:
                ans = 79526.611536
                ans2 = 78992.875888
                if (w < ans - tol) or (w > ans + tol):
                    print(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from left to right)!'
                        % ind
                    )
                    flag_left = True
                if (w < ans2 - tol) or (w > ans2 + tol):
                    print(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from right to left)!'
                        % ind
                    )
                    flag_right = True
                if flag_left and flag_right:
                    print(
                        "[FAILED} Test %d: Wrong TSP considering both directions of DFS traversal"
                        % ind
                    )
                    Tflag = True
                if (flag_left or flag_right) and not Tflag:
                    print("Test %d still passed." % ind)
        else:
            Tflag = True
        if not Mflag:
            Mpass += 1
        if not Tflag:
            Tpass += 1

    s = 'Passed %d/%d MST Tests and %d/%d TSP Tests.' % (Mpass, t, Tpass, t)
    return s


##############################################################################


def test2approx():
    """
    Tests your code on the various maps using getTSPOptimal.

    Returns:
        s (str): a string indicating number of tests passed.
    """
    passed = 0
    t = 4

    # Check if the approximate solution is a 2-approximation.
    for ind in range(0, t):
        m = Map(ind)
        m.getMST()
        m.getTSPApprox()
        wA = 0
        for r in range(0, len(m.tour) - 1):
            wA += m.adjMat[m.tour[r]][m.tour[r + 1]]

        m.getTSPOptimal()
        wO = 0
        for r in range(0, len(m.tourOpt) - 1):
            wO += m.adjMat[m.tourOpt[r]][m.tourOpt[r + 1]]

        if wA <= 2 * wO:
            passed += 1

    s = 'Passed %d/%d 2-approximation tests.' % (passed, t)
    return s
