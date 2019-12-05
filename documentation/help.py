#!/usr/bin/env python

def print_help():
    print("""Geometry Problem Solver: Help Section
                The two problems that the can be solved:
                    - Circle and Triangle
                    - Line and Triangle
                The Program is to solve the two images satisfying
                at most 3 geometric predicates.
                The following predicates are applicable to the two
                problems presented in the images displayed.
                Usage is listed along with each predicate.
                Predicate & Usage:
                    >> set_parallel(name1, name2)
                        Ex: >> set_parallel(s2, s6)
                    >> set_perpendicular(name1, name2)
                        Ex: >> set_perpendicular(s8, s9)
                    >> set_equal(name1, name2, fraction)
                        Ex: >> set_fraction(s8,s9, 1/4 )
                    >> set_sum_value(name1, name2, sum)
                        Ex: >> set_sum_value(a7, a8, 90)
                    >> set_congruent(name1, name2)
                        Ex: set_congruent(ar1, ar7)
                    >> set_tan(name1, name2)
                        Ex: set_tan(s2,s4)
                Inputs can be atmost 3 geomertic predicates.
                    >> set_parallel(name1, name2), set_perpendicular(name3, name4), set_fraction(name5, name6, n)
                Prepend the name of the problem to solve:
                    >> Circle and Triangle set_parallel(name1, name2), set_perpendicular(name3, name4), set_fraction(name5, name6, n)
          """)
