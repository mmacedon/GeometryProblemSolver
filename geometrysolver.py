#!/usr/bin/env python
import documentation.license
import documentation.help
from helperfunctions import *
from A242 import *
from A142 import *

try:
    from PIL import Image
except:
    print("""Import Error: Module Image required for
              GeometryProblemSolver not found.
              Run: pip install Image
              Restart Code.
                """)
    exit(1)

def display_images():

    image = Image.open('./img/Circle and Triangle 14.JPG')
    image_2 = Image.open('./img/Line and Triangle 1.JPG')
    if ( image == None or image_2 == None ):
        return -1
    else:
        image.show()
        image_2.show()
    return 0

def main():

    print("Welcome to Geometry Problem Solver")
    print("""
            For Usage of Program: Input Three or More Predicates in the Following
            Format: [problem] [predicate name](parameter_1, parameter_2,..., parameter_n)
            The Problems are:
                - Circle and Triangle
                - Line and Triangle
            Use the images presented to choose the parameters.
            Allow the images to load.
            For Help: -help
            For License: -license
            For Testing: -test
            For Exiting: -quit
            GitHub: https://github.com/mmacedon/GeometryProblemSolver
        """)

    #Display the Images to the User
    success = display_images()
    if ( success == -1 ):
        print("""Image Error: Make sure that the two images 'Circle and Triangle 14.JPG'
                    and 'Line and Triangle 1.JPG' are in the directory ./GeometryProblemSolver/img/.
                    For redownloading the images, visit the Github link. Place within directory and
                    restart code.""")
        exit(1)

    while ( True ):
        user_input = input(">> ")
        if ( user_input == "-quit" ):
            break
        elif ( user_input == "-license"):
            documentation.license.print_license()
        elif ( user_input == "-help"):
            documentation.help.print_help()
        elif ( user_input == "-test"):
            run_test()
        elif ("Line" in user_input or "line" in user_input):
            solver_problem_1(user_input)
        elif("circle" in user_input or "Circle" in user_input):
            parsed_input = parseinput(user_input)
            solver_problem_2(parsed_input)
        else:
            print("Invalid Input\n")
            print("Enter -help for help using the solver.")

    print("Thank you for using the Geometry Solver\n")
    return 0

if __name__ == '__main__':
    main()
