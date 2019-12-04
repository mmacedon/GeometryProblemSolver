#!/usr/bin/env python

def verify_user_input(allowed, input):

    verified = 1

    for i in range(len(input)):
        for j in range(len(input[i][1])):
            current = input[i][1][j]
            if current in allowed:
                continue
            else:
                verified = 0
    return verified

def parseinput( input ):

    input = input.split('set')
    problem = input[0]
    predicates = input[1:]

    for i in range(len(predicates)):
        predicates[i] = ('set' + predicates[i]).strip()
        predicates[i] = predicates[i]

    variables = []
    temporary_predicate_holder = []
    for predicate in predicates:
        x = predicate.split(',')
        y = x[0].split('(')
        temporary_predicate_holder.append(y[0])
        variables.append(y[1])
        for i in range(len(x) - 1):
           variables.append(x[i+1])
    variables.append('')

    parsed_input = []

    vars = []
    i = 0
    predicate = temporary_predicate_holder[i]
    for var in variables:
        if var == '':
            parsed_input.append([predicate, vars])
            i = (i + 1) % (len(temporary_predicate_holder))
            predicate = temporary_predicate_holder[i]
            vars = []
        else:
            vars.append(var)

    for i in range(len(parsed_input)):
        for j in range(len(parsed_input[i][1])):
            current = parsed_input[i][1][j]
            if ( ' ' in current and ')' in current):
                current = current.split(' ')
                current = current[1]
                current = current.split(')')
                current = current[0]
                parsed_input[i][1][j] = current
            elif ( ' ' in current ):
                current = current.split(' ')
                current = current[1]
                parsed_input[i][1][j] = current

    return parsed_input
