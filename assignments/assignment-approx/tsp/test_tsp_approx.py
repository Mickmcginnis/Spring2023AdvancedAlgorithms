"""
Advanced Algorithms HW2 Testing Functions for tsp_approx_starter.py
"""

import math
import pytest
from tsp_approx_starter import Map
import warnings

##############################################################################
# The following functions generate test maps to run the algorithm on!


def testMSTApprox():
    """
    Tests your code on the various maps.
    """
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

        if m.mst != None:
            m.getTSPApprox()
            w = 0
            if len(m.tour) > 0:
                for r in range(0, len(m.tour) - 1):
                    w += m.adjMat[m.tour[r]][m.tour[r + 1]]
            else:
                w = math.inf
            if len(m.tour) != len(m.cities) + 1:
                warnings.warn(
                    'Test %d: TSP should be length %d.' % (ind, len(m.cities) + 1)
                )

            if w == math.inf:
                warnings.warn('Test %d: No TSP reported.' % ind)

            else:
                if w > 2 * MSTw + 2 * tol:
                    warnings.warn('Test %d: TSP too large.' % ind)

                if w <= MSTw - tol:
                    warnings.warn('Test %d: TSP too small.' % ind)

            if len(m.tour) > 0:
                if m.tour[0] != m.tour[-1]:
                    warnings.warn('Test %d: TSP start != end.' % ind)

            for c in range(1, len(m.tour)):
                city = m.tour[c]
                if city in m.tour[c + 1 :]:
                    warnings.warn('Test %d: Repeated City in TSP.' % ind)

            if ind == 7:
                ans = 40030.173592
                ans2 = 78992.875888
                if (w < ans - tol) or (w > ans + tol):
                    warnings.warn(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from left to right)!'
                        % ind
                    )
                    flag_left = True
                if (w < ans2 - tol) or (w > ans2 + tol):
                    warnings.warn(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from right to left)!'
                        % ind
                    )
                    flag_right = True
                if flag_left and flag_right:
                    pytest.fail(
                        "[FAILED] Test %d: Wrong TSP considering both directions of DFS traversal"
                        % ind
                    )

            if ind == 8:
                ans = 79526.611536
                ans2 = 78992.875888
                if (w < ans - tol) or (w > ans + tol):
                    warnings.warn(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from left to right)!'
                        % ind
                    )
                    flag_left = True
                if (w < ans2 - tol) or (w > ans2 + tol):
                    warnings.warn(
                        'Test %d: Wrong TSP (when traversing the tree via DFS from right to left)!'
                        % ind
                    )
                    flag_right = True
                if flag_left and flag_right:
                    pytest.fail(
                        "[FAILED] Test %d: Wrong TSP considering both directions of DFS traversal"
                        % ind
                    )


##############################################################################


def test2approx():
    """
    Tests your code on the various maps using getTSPOptimal.
    """
    t = 4  # number of tests

    # Check if the approximate solution is a 2-approximation.
    for ind in range(0, t):
        m = Map(ind)
        m.getMST()
        m.getTSPApprox()

        if len(m.tour) > 0:
            wA = 0
            for r in range(0, len(m.tour) - 1):
                wA += m.adjMat[m.tour[r]][m.tour[r + 1]]

            m.getTSPOptimal()
            wO = 0
            for r in range(0, len(m.tourOpt) - 1):
                wO += m.adjMat[m.tourOpt[r]][m.tourOpt[r + 1]]

            if wA > 2 * wO:
                pytest.fail(
                    '[FAILED] Test %d: TSP index %d weight is not 2-approximation, compared to optimal weight'
                    % (ind + 1, ind)
                )
        else:
            pytest.fail('[FAILED] Test 0: Tour length < 1, invalid tour length')
