#!/usr/bin/env python

def main():
    print("Welcome to Geometry Problem Solver")
    print("""
            For Usage of Program: Input Three or More Predicates in the Following
            Format: [predicate name](parameter_1, parameter_2,..., parameter_n)
            Use the images presented to choose the parameters.
            For Help: -help
            For License: -license
            For Exiting: -quit
            Code Can Be Found on GitHub: https://github.com/mmacedon/GeometryProblemSolver
        """)

    while ( True ):
        user_input = input(">> ")
        if ( user_input == "-quit" ):
            print("Thank you for using the Geometry Solver\n")
            break
        elif ( user_input == "-license"):
            license.printlicense()
        elif ( user_input == "-help"):
            help.printhelp()
        else:
            solver(user_input)

    return 0

if __name__ == '__main__':
    main()
