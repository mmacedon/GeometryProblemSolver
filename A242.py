#!/usr/bin/env python
from helperfunctions import *
import random
#Circle and triangle

#Prependicular is ommitted since there are no possible ways to
#make perpendicular lines in the Circle and Triangle Problem

class parallel():
    def __init__(self):
        self.relationships = []

    def make_parallel(self, a, b):
        if [a, b] in self.relationships or [b,a] in self.relationships:
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False

class perpendicular:
    def __init__(self):
        self.relationships = []

    def make_perpendicular(self, a, b):
        if [a, b] in self.relationships or [b,a] in self.relationships or len(self.relationships) == 1:
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False

#equal being used as a descriptor of length, angle or area
class equal:
    def __init__(self):
        self.relationships = []

    def make_equal(self, a, b):
        if [a, b] in self.relationships or [b,a] in self.relationships:
            print("Returning")
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False


class fraction:
    def __init__(self):
        self.relationships = []

    def make_fraction(self, a, b, n):
        if [a, b, n] in self.relationships or [b, a, n] in self.relationships:
            return
        else:
            self.relationships.append([a, b, n])

    def has(self, a, b):
        for relation in self.relationships:
            if (a == relation[0] and b == relation[1]) or (a == relation[1] and b == relation[0]):
                return True
        else:
            return False

    def get_fraction(self, a, b):
        for relationship in self.relationships:
            if (relationship[0] == a and relationship[1] == b) or (relationship[0] == b and relationship[1] == a):
                return relationship[2]

class sum_value:
    def __init__(self):
        self.relationships = []

    def make_sum_value(self, a, b, n):
        if [a, b, n] in self.relationships or [b, a, n] in self.relationships:
            return
        else:
            self.relationships.append([a,b, n])

    def has(self, a, b):
        for relation in self.relationships:
            if (a == relation[0] and b == relation[1]) or (a == relation[1] and b == relation[0]):
                return True
        else:
            return False

    def get_sum_value(self, a, b):
        for relationship in self.relationships:
            if (relationship[0] == a and relationship[1] == b) or (relationship[0] == b and relationship[1] == a):
                return relationship[2]

class similar:
    def __init__(self):
        self.relationships = []

    def make_similar(self, a, b):
        if [a, b] in self.relationships or [b, a] in self.relationships:
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a, b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False

class congruent:
    def __init__(self):
        self.relationships = []

    def make_congruent(self, a, b):
        if [a, b] in self.relationships or [b,a] in self.relationships:
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a, b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False


class tan:
    def __init__(self):
        self.relationships = []

    def make_tan(self, a, b):
        if [a, b] in self.relationships or [b, a] in self.relationships:
            return
        else:
            self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False


#actual object instanciation
parallel_predicate = parallel()
perpendicular_predicate = perpendicular()
equal_predicate = equal()
fraction_predicate = fraction()
sum_value_predicate = sum_value()
similar_predicate = similar()
congruent_predicate = congruent()
tan_predicate = tan()

#DEF CHECK_EQUAL_FRACTION_PREDICATES
def reset_predicates():
    parallel_predicate.relationships = []
    perpendicular_predicate.relationships = []
    equal_predicate.relationships = []
    fraction_predicate.relationships = []
    sum_value_predicate.relationships = []
    similar_predicate.relationships = []
    congruent_predicate.relationships = []
    tan_predicate.relationships = []


def set_parallel(name1, name2): #When a “parallel” predicate is given
    if parallel_predicate.has(name1, name2):
        return False

    parallel_predicate.make_parallel(name1, name2)#calls function that actually makes them parallel
    print("\nParallel Inputs: %s %s\n" % (name1, name2))

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()

def set_perpendicular(name1, name2): #When a “perpendicular” predicate is given
    if perpendicular_predicate.has(name1, name2):
        return False

    perpendicular_predicate.make_perpendicular(name1, name2)#calls function that actually makes them perpendicular
    print("\nPerpendicular Inputs: %s %s\n" % (name1, name2))
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()

def set_equal(name1, name2): #Similar to above
    if equal_predicate.has(name1, name2):
        return False

    equal_predicate.make_equal(name1, name2)#calls function that actually makes them parallel
    print("\nEqual Inputs: %s %s\n" % (name1, name2))
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()


def set_fraction(name1, name2,fraction):
    if fraction_predicate.has(name1, name2):
        return False
    fraction_predicate.make_fraction(name1, name2, fraction)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()

def set_sum_value(name1, name2,sum): #When a “parallel” predicate is given
    if sum_value_predicate.has(name1, name2):
        return False

    sum_value_predicate.make_sum_value(name1, name2,sum)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()

def set_similar(name1, name2): #When a “parallel” predicate ==given
    if similar_predicate.has(name1, name2):
        return False
    similar_predicate.make_similar(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()


def set_congruent(name1, name2): #When a “parallel” predicate ==given

    if congruent_predicate.has(name1, name2):
        return False

    congruent_predicate.make_congruent(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later

    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()

def set_tan(name1, name2): #When a “parallel” predicate ==given
    if tan_predicate.has(name1, name2):
        return False

    tan_predicate.make_tan(name1, name2)#calls function that actually makes them parallel
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later

    if name1 =='s1':
        know_s1()
    elif name1 =='s2':
        know_s2()
    elif name1 =='s3':
        know_s3()
    elif name1 =='s4':
        know_s4()
    elif name1 =='s5':
        know_s5()
    elif name1 =='s6':
        know_s6()
    elif name1 =='s7':
        know_s7()
    elif name1 =='a1':
        know_a1()
    elif name1 =='a2':
        know_a2()
    elif name1 =='a3':
        know_a3()
    elif name1 =='arc1':
        know_arc1()
    elif name1 =='arc3':
        know_arc3()
    elif name1 =='arc4':
        know_arc4()
    elif name1 =='arc5':
        know_arc5()

    if name2 =='s1':
        know_s1()
    elif name2 =='s2':
        know_s2()
    elif name2 =='s3':
        know_s3()
    elif name2 =='s4':
        know_s4()
    elif name2 =='s5':
        know_s5()
    elif name2 =='s6':
        know_s6()
    elif name2 =='s7':
        know_s7()
    elif name2 =='a1':
        know_a1()
    elif name2 =='a2':
        know_a2()
    elif name2 =='a3':
        know_a3()
    elif name2 =='arc1':
        know_arc1()
    elif name2 =='arc3':
        know_arc3()
    elif name2 =='arc4':
        know_arc4()
    elif name2 =='arc5':
        know_arc5()




#some left as skeleton functions for testing, since calling them ==mandatory for functionality
#FOR THE SET FRACTIONS, INVESTIGATE WHETHER S3 CAN BE SET EQUAL TO ANY OTHER LINE
#FOR FRACTIONS; SEE IF FOLLOWING CONDITION APPLIES
# IF (S1 = FRAC_1 * S2 AND S2 == S4) AND (S5 = S4 * FRAC_2) AND FRAC_1 == FRAC_2 THEN S1 == S5
def check_equal_predicates(name1):
    names = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']

    for name2 in names:
        if not equal_predicate.has(name1, name2):
            continue
        if name1 == name2:
            continue
        for relation in equal_predicate.relationships:
            if name1 in relation:
                continue
            if name2 == relation[0] or name2 == relation[1]:
                new = relation[0] if name2 == relation[1] else relation[1]
                if not equal_predicate.has(name1, new):
                   set_equal(name1, new)

def check_fractional_predicates(name1):
    names = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
    for name2 in names:
        if not fraction_predicate.has(name1, name2):
            continue
        if name1 == name2:
            continue
        for relation in equal_predicate.relationships:
            if name1 in relation:
                continue
            if name2 == relation[0] or name2 == relation[1]:
                new = relation[0] if name2 == relation[1] else relation[1]
                if not fraction_predicate.has(name1, new):
                   set_fraction(name1, new, fraction_predicate.get_fraction(name1, name2))

def check_similarities():
    #Only 3 conditions to check (ar2, ar5) (ar6, ar4) (ar6, ar3), (ar3, ar4)
    if fraction_predicate.has('s1' , 's5') and fraction_predicate.has('arc1', 'arc4'):
        set_similar('ar2', 'ar5')

    if equal_predicate.has('a1', 'a2') and fraction_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3'):
        set_similar('ar4', 'ar3')


    if equal_predicate.has('a1', 'a2') and ((fraction_predicate.has('s7', 's2') and fraction_predicate.has('s6', 's3')) or (fraction_predicate.has('s7', 's3') and fraction_predicate.has('s6', 's2'))):
        set_similar('ar4', 'ar6')

    if equal_predicate.has('a1', 'a2') and ((fraction_predicate.has('s7', 's4') and fraction_predicate.has('s6', 's3')) or (fraction_predicate.has('s7', 's3') and fraction_predicate.has('s6', 's4'))):
        set_similar('ar3', 'ar6')

def know_s1():

    #Consider what knowing S1 reveals about the rest of the Problem
    #If S1 is equal to S5 and Arc1 is equal to arc3, then we know ar2 and ar5 are equal
    #Really gotta cover all know cases.
    #This is gonna be a long night

    #SET EQUAL PREDICATE
    if equal_predicate.has('s1', 's5') and equal_predicate.has('arc1', 'arc4'):
        set_equal('ar2','ar5')
        set_congruent('ar2', 'ar5')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('ar2','ar5'):
        set_equal('arc1','arc4')

    if equal_predicate.has('s1','s5') and equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s6', 's7')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7') and equal_predicate.has('a1', 'a2'):
        set_equal('s2', 's4')

    check_equal_predicates('s1')

    #SET FRACTION PREDICATE
    if fraction_predicate.has('s1', 's2'):
        set_fraction('s1', 's4', fraction_predicate.get_fraction('s1', 's2'))
    elif fraction_predicate.has('s1', 's4'):
        set_fraction('s1', 's2', fraction_predicate.get_fraction('s1', 's2'))

    if fraction_predicate.has('s1', 'arc1') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('s5', 'arc4', fraction_predicate.get_fraction('s1', 'arc1'))
    elif fraction_predicate.has('s1', 's5') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('arc1', 'arc4', fraction_predicate.get_fraction('s1', 's5'))
    elif fraction_predicate.has('s1', 'arc4') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('s5', 'arc1', fraction_predicate.get_fraction('s1', 's4'))

    #EXHAUST ALL THE FRACTION COMBINATIONS
    check_fractional_predicates('s1')

    #SET SUM VALUE #SKIP FOR NOW #Relationship does not tell you anything new about the problem
    #MAY SKIP? WE'LL SEE


def know_s2():

    #SET_PERPENDICULAR
    if perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4') and not perpendicular_predicate.has('s7', 's6'):
        set_sum_value('a2', 'a3', '90')

    #SET_EQUAL
    if equal_predicate.has('s2', 's4') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s7', 's6')
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('s7', 's6') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s4', 's7') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s4', 's7')
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's7'):
        set_equal('a1', 'a2')
    if equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2'):
        set_equal('ar3', 'ar4')
        set_congruent('ar3', 'ar4')
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('ar3', 'ar4') and equal_predicate.has('a1', 'a2'):
        set_tan('s3', 'arc3')

    elif equal_predicate.has('s2', 's4') and equal_predicate.has('ar3', 'ar4') and tan_predicate.has('s3', 'arc3'):
        set_equal('a1', 'a2')

    check_equal_predicates('s2')


    #No way I can think of if S2 is equal to S3 or S2 equal to S1 or S5.
    #Don't learn anything new

    #SET FRACTION #A = B * n
    ## Double check this one
    if fraction_predicate.has('s3', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar3'):
        set_fraction('s3', 's4', fraction_predicate.get_fraction('s3', 's2'))
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and equal_predicate.has('ar3', 'ar4'):
        set_equal('a1', 'a2')

    if fraction_predicate.has('s1', 's2') and equal_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        set_fraction('s5', 's2', fraction_predicate.get_fraction('s1', 's2'))

    elif fraction_predicate.has('s5', 's2') and equal_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        set_fraction('s1', 's2', fraction_predicate.get_fraction('s5', 's2'))


    if fraction_predicate.has('s2', 's3') and equal_predicate.has('ar4', 'ar3'):
        set_fraction('s3', 's4', fraction_predicate.get_fraction('s2', 's3'))
    elif fraction_predicate.has('s2', 's3') and fraction_predicate.has('s3', 's4') and equal.has('a1', 'a2'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and equal_predicate.has('ar4', 'ar3'):
        set_equal('a1', 'a3')

    check_fractional_predicates('s2')
#EXHAUSTED ALL THE POSSIBLE COMBINATIONS I CAN THINK OF

#KNOWING SUM VALUE DOES NOT PRODUCE ANYTHING NEW THAT I CAN THINK OF OR USEFUL INFORMATION
#SET SIMILAR SCRAPPED
#CONGRUENT: LINES CANNOT BE congruent
#S2 CANNOT BE SET TANGENT. AT LEAST I DON'T THINK, LET'S AWAIT WHAT THE TA SAYS


def know_s3():
    #SET PARALLEL DOES NOT apply
    #SET perpendicular
    if perpendicular_predicate.has('s3', 's2') and not perpendicular_predicate.has('s3', 's4') and not perpendicular_predicate.has('s7', 's6'):
        set_sum_value('a2', 'a3', '90')
    elif perpendicular_predicate.has('s3', 's4') and not perpendicular_predicate.has('s3', 's2') and not perpendicular_predicate.has('s7', 's6'):
        set_sum_value('a1', 'a3', '90')

    #set EQUAL #not sure how this can be done
    #SET tangent
    if tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2') and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4') and equal_predicate.has('ar4', 'ar3') and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('a1', 'a2')
    elif tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar3', 'ar4') and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('s2', 's4')

    #SET_FRACTION
    if fraction_predicate.has('s3', 's2') and equal_predicate.has('s2', 's4'):
        set_fraction('s3', 's4', fraction_predicate.get_fraction('s3', 's2'))
    elif fraction_predicate.has('s3', 's4') and equal_predicate.has('s2', 's4'):
        set_fraction('s3','s2', fraction_predicate.get_fraction('s3', 's4'))


    #CAN THE SIDE S3 BE SMALLER THAN ANY OTHER SIDE S, OR MUST IT BE THE BIGGEST
    #SINCE IT IS A STAND ALONE SIDE
    #SET SUM VALUE DOES NOT TELL ANYTHING INTERESTING
    #SET SIMILAR NOT required
    #SET CONGRUENT NOT POSSIBLE FOR LINE S3




def know_s4():
        #s4 very similar to s2

    if perpendicular_predicate.has('s4', 's3') and not perpendicular_predicate.has('s3', 's2') and not perpendicular_predicate.has('s7', 's6'):
        set_sum_value('a1', 'a3', '90')

    #SET_EQUAL
    if equal_predicate.has('s4', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s7', 's6')
    elif equal_predicate.has('s4', 's2') and equal_predicate.has('s7', 's6') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s4', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s2', 's6') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s2', 's6')
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's6'):
        set_equal('a1', 'a2')

    if equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2'):
        set_equal('ar3', 'ar4')
        set_congruent('ar3', 'ar4')
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('ar3', 'ar4') and equal_predicate.has('a1', 'a2'):
        set_tan('s3', 'arc3')
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('ar3', 'ar4') and tan_predicate.has('s3', 'arc3'):
        set_equal('a1', 'a2')


    check_equal_predicates('s4')
    #No way I can think of if S2 is equal to S3 or S2 equal to S1 or S5.
    #Don't learn anything new

    #SET FRACTION #A = B * n
## Double check this one
    if fraction_predicate.has('s3', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar3'):
        set_fraction('s3', 's2', fraction_predicate.get_fraction('s3', 's4'))
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and equal_predicate.has('a1', 'a2'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and equal_predicate.has('ar3', 'ar4'):
        set_equal('a1', 'a2')

    if fraction_predicate.has('s1', 's4') and equal_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        set_fraction('s5', 's4', fraction_predicate.get_fraction('s1', 's4'))
    elif fraction_predicate.has('s5', 's4') and equal_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        set_fraction('s1', 's4', fraction_predicate.get_fraction('s5', 's4'))

    if fraction_predicate.has('s4', 's3') and equal_predicate.has('ar4', 'ar3'):
        set_fraction('s3', 's2', fraction_predicate.get_fraction('s4', 's3'))
    elif fraction_predicate.has('s4', 's3') and fraction_predicate.has('s3', 's2') and equal.has('a1', 'a2'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and equal_predicate.has('ar4', 'ar3'):
        set_equal('a1', 'a3')


    check_fractional_predicates('s4')

    #SET SUM VALUE DOES NOT TELL US ANYTHING NEW AS AN INPUT FOR lines
    #SET CONGRUENT ONLY FOR AREAS NOT LINES
    #S4 CANNOT BE SET TANGENT IN THIS CASE


def know_s5():

    if equal_predicate.has('s1', 's5') and equal_predicate.has('arc1', 'arc4'):
        set_equal('ar2','ar5')
        set_congruent('ar2', 'ar5')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('ar2','ar5'):
        set_equal('arc1','arc4')
    if equal_predicate.has('s1','s5') and equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s6', 's7')
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7') and equal_predicate.has('a1', 'a2'):
        set_equal('s2', 's4')

    check_equal_predicates('s5')
    #SET FRACTION PREDICATE
    if fraction_predicate.has('s5', 's2'):
        set_fraction('s5', 's4', fraction_predicate.get_fraction('s5', 's2'))
    elif fraction_predicate.has('s5', 's4'):
        set_fraction('s5', 's2', fraction_predicate.get_fraction('s5', 's4'))

    if fraction_predicate.has('s5', 'arc5') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('s1', 'arc1', fraction_predicate.get_fraction('s5', 'arc5'))
    elif fraction_predicate.has('s1', 's5') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('arc1', 'arc4', fraction_predicate.get_fraction('s1', 's5'))
    elif fraction_predicate.has('s5', 'arc1') and equal_predicate.has('ar2', 'ar5'):
        set_fraction('s1', 'arc4', fraction_predicate.get_fraction('s5', 'arc1'))


    #EXHAUST ALL THE FRACTION COMBINATIONS
    check_fractional_predicates('s5')


def know_s6():
    # s6 cannot be set parallel to any LINES

    #set perpendicular
    if perpendicular_predicate.has('s6', 's7') and not perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4'):
        set_sum_value('a1', 'a2', '90')

    #SET EQUAL
    if equal_predicate.has('s6', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s7', 's4')
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's7'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s2', 's4')
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')

    check_equal_predicates('s6')
    #SET FRACTION

    #SET SUM VALUE DOES NOT TELL ANYTHING NEW ABOUT THE SHAPE
    #SET SIMILAR DOES NOT apply IN THIS CASE
    #SET CONGRUENT IS NOT POSSIBLE FOR LINES
    #This one concerns with fraction = 2
    if equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.get_fraction('s3', 's7') == '2' and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'arc3')
    elif equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_fraction('arc3', 'arc5', '2')
    elif equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_fraction('s3', 's7', '2')
    elif equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7') and fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('ar3', 'ar6') and fraction_predicate.get_fraction('s3', 's7') == '2'  and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_equal('a1', 'a2')

    if equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_fraction('arc3', 'arc5', '2')
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.get_fraction('arc3', 'arc57') == '2':
        set_fraction('s3', 's7', '2')
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('a1', 'a2')


    #SET SUM VALUE DOES NOT TELL ANYTHING UNIQUE ABOUT THE LINES
    #SET SIMILAR DOES NOT apply TO THIS CASE
    #SET CONGRUENT DOES NOT apply IN THIS CASE
    #CANNOT BE SET TAN TO ANYTHING
    check_fractional_predicates('s6')

def know_s7():
    # s7 cannot be set parallel to any LINES

    #set perpendicular
    if perpendicular_predicate.has('s7', 's6') and not perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4'):
        set_sum_value('a1', 'a2', '90')
    #SET EQUAL
    if equal_predicate.has('s7', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s6', 's4')
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's6'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('s1', 's5')
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        set_equal('s2', 's4')
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')

    check_equal_predicates('s7')
    #SET FRACTION

    #SET SUM VALUE DOES NOT TELL ANYTHING NEW ABOUT THE SHAPE
    #SET SIMILAR DOES NOT apply IN THIS CASE
    #SET CONGRUENT IS NOT POSSIBLE FOR LINES
    #This one also concerns 2
    if equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.has('arc3', 'arc5'):
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6'):
        set_fraction('arc3', 'arc5', '2')
    elif equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.has('arc3', 'arc5'):
        set_fraction('s3', 's6', '2')
    elif equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6') and fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('ar3', 'ar6'):
        set_equal('a1', 'a2')

    if equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.has('arc3', 'arc5'):
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6'):
        set_fraction('arc3', 'arc5', '2')
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5'):
        set_fraction('s3', 's6', '2')
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5') and fraction_predicate.has('s3', 's6'):
        set_equal('a1', 'a2')


    check_fractional_predicates('s7')

    #SET SUM VALUE DOES NOT TELL ANYTHING UNIQUE ABOUT THE LINES
    #SET SIMILAR DOES NOT apply TO THIS CASE
    #SET CONGRUENT DOES NOT apply IN THIS CASE
    #CANNOT BE SET TAN TO ANYTHING

def know_a1():

    #SET EQUAL
    if equal_predicate.has('a1', 'a2') and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_tan('s3', 'arc3')

    if equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        set_equal('s6', 's7')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's4') and equal_predicate.has('s6', 's7'):
        set_equal('s1', 's5')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        set_equal('s2', 's4')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's4') and equal_predicate.has('s2', 's6'):
        set_equal('s5', 's7')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's6') and equal_predicate.has('s5', 's7'):
        set_equal('s1', 's4')
    elif set_equal('a1', 'a2') and equal_predicate.has('s5', 's7') and equal_predicate.has('s1', 's4'):
        set_equal('s2', 's6')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's6') and equal_predicate.has('s2', 's5'):
        set_equal('s4', 's7')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's5') and equal_predicate.has('s4', 's7'):
        set_equal('s1', 's6')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's6'):
        set_equal('s2', 's5')

    if equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif equal_predicate.has('a1', 'a2') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('ar4', 'ar3'):
        set_equal('s2', 's4')
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
        set_tan('s3', 'arc3')

    #SET FRACTION
    #This one concerns 2
    if fraction_predicate.has('a1', 'a2') and sum_value_predicate.has('a2', 'a3') and fraction_predicate.get_fraction('a1', 'a2') == '2' and sum_value_predicate.get_sum_value('a2', 'a3') == '90':
        set_fraction('a1', 'a3', '2')
        set_equal('a2', 'a3')
        set_perpendicular('s2', 's3')
    elif fraction_predicate.has('a1', 'a3') and sum_value_predicate.has('a2', 'a3') and fraction_predicate.get_fraction('a1', 'a3') == '2' and sum_value_predicate.get_sum_value('a2', 'a3') == '90':
        set_fraction('a1', 'a2', '2')
        set_equal('a2', 'a3')
        set_perpendicular('s2', 's3')

    #SET SUM VALUE
    if sum_value_predicate.has('a1', 'a2') and sum_value_predicate.get_sum_value('a1', 'a2') == '90':
        set_perpendicular('s6', 's7')
    elif sum_value_predicate.has('a1', 'a3') and sum_value_predicate.get_sum_value('a1', 'a3') == '90':
        set_perpendicular('s3', 's4')


def know_a2():
    #SET EQUAL
    if equal_predicate.has('a2', 'a1') and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_tan('s3', 'arc3')

    if equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        set_equal('s6', 's7')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's4') and equal_predicate.has('s6', 's7'):
        set_equal('s1', 's5')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        set_equal('s2', 's4')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's4') and equal_predicate.has('s2', 's6'):
        set_equal('s5', 's7')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's6') and equal_predicate.has('s5', 's7'):
        set_equal('s1', 's4')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s5', 's7') and equal_predicate.has('s1', 's4'):
        set_equal('s2', 's6')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's6') and equal_predicate.has('s2', 's5'):
        set_equal('s4', 's7')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's5') and equal_predicate.has('s4', 's7'):
        set_equal('s1', 's6')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's6'):
        set_equal('s2', 's5')
    if equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif equal_predicate.has('a2', 'a1') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('ar4', 'ar3'):
        set_equal('s2', 's4')
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
        set_tan('s3', 'arc3')



    #SET FRACTION
    if fraction_predicate.has('a2', 'a1') and sum_value_predicate.has('a1', 'a3') and fraction_predicate.get_fraction('a2', 'a1') == '2' and sum_value_predicate.get_sum_value('a1', 'a3') == '90':
        set_fraction('a2', 'a3', '2')
        set_equal('a1', 'a3')
        set_perpendicular('s4', 's3')
    elif fraction_predicate.has('a2', 'a3') and sum_value_predicate.has('a1', 'a3') and fraction_predicate.get_fraction('a2', 'a3') == '2' and sum_value_predicate.get_sum_value('a1', 'a3') == '90':
        set_fraction('a2', 'a1', '2')
        set_equal('a1', 'a3')
        set_perpendicular('s4', 's3')


    #SET SUM VALUE
    if sum_value_predicate.has('a2', 'a1') and sum_value_predicate.get_sum_value('a2', 'a1') == '90':
        set_perpendicular('s6', 's7')
    elif sum_value_predicate.has('a2', 'a3') and sum_value_predicate.get_sum_value('a2', 'a3') == '90':
        set_perpendicular('s2', 's3')

def know_a3():

    if equal_predicate.has('a3', 'a1') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's2') and fraction_predicate.has('s6', 's3'):
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('s7', 's2') and fraction_predicate.has('s6', 's3') and equal_predicate.has('ar4', 'ar6'):
        set_tan('s3', 'arc3')
    elif equal_predicate.has('a3', 'a1') and fraction_predicate.has('s6', 's3') and equal_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3'):
        set_equal('s7', 's2')
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's2'):
        set_fraction('s6', 's3', '2')
    elif equal_predicate.has('a3', 'a1') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's2') and fraction_predicate.has('s7', 's3'):
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('s6', 's2') and fraction_predicate.has('s7', 's3') and equal_predicate.has('ar4', 'ar6'):
        set_tan('s3', 'arc3')
    elif equal_predicate.has('a3', 'a1') and fraction_predicate.has('s7', 's3') and equal_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3'):
        set_equal('s6', 's2')
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's2'):
        set_fraction('s7', 's3', '2')

    if equal_predicate.has('a3', 'a2') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s6', 's3'):
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s6', 's3') and equal_predicate.has('ar3', 'ar6'):
        set_tan('s3', 'arc3')
    elif equal_predicate.has('a3', 'a2') and fraction_predicate.has('s6', 's3') and equal_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3'):
        set_equal('s7', 's4')
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's4'):
        set_fraction('s6', 's3', '2')
    elif equal_predicate.has('a3', 'a2') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s7', 's3'):
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s7', 's3') and equal_predicate.has('ar3', 'ar6'):
        set_tan('s3', 'arc3')
    elif equal_predicate.has('a3', 'a2') and fraction_predicate.has('s7', 's3') and equal_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3'):
        set_equal('s6', 's4')
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's4'):
        set_fraction('s7', 's3', '2')

    #SET FRACTION
    if fraction_predicate.has('a3', 'a1') and sum_value_predicate.has('a1', 'a2') and sum_value_predicate.get_sum_value('a1', 'a2') == '90':
        set_fraction('a3', 'a2', '2')
        set_equal('a1', 'a2')
        set_perpendicular('s6', 's7')
    elif fraction_predicate.has('a3', 'a2') and sum_value_predicate.has('a1', 'a2') and sum_value_predicate.get_sum_value('a1', 'a2') == '90':
        set_fraction('a3', 'a1', '2')
        set_equal('a1', 'a2')
        set_perpendicular('s6', 's7')

    #SET SUM_VALUE
    if sum_value_predicate.has('a3', 'a1') and sum_value_predicate.get_sum_value('a3', 'a1') == '90':
        set_perpendicular('s3', 's4')
    elif sum_value_predicate.has('a3', 'a2')  and sum_value_predicate.get_sum_value('a3', 'a2') == '90':
        set_perpendicular('s2', 's3')

def know_ar1():
    print("Knowing ar1 does not define anything else in the problem.\n")

def know_ar2():

    #set_parallel does not apply
    #set_perpendicular does not apply
    #set_sum_value does not tell anything about this problem
    #   equal
    if equal_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        set_equal('s1', 's5')
    elif equal_predicate.has('ar2', 'ar5') and equal_predicate.has('s1', 's5'):
        set_equal('arc1', 'arc4')
    # set_tan does not apply

def know_ar3():
    #set_parallel does not apply
    #set_perpendicular does not apply
    #set_equal
    if equal_predicate.has('ar3', 'ar4') and equal_predicate.has('a1', 'a2') and tan_predicate.has('s3', 'arc3'):
        set_equal('s2', 's4')
    elif equal_predicate.has('ar3', 'ar4') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('ar3', 'ar4') and equal_predicate.has('s2', 's4') and equal_predicate.has('ar4', 'ar3'):
        set_tan('s3', 'arc3')
    #set sum value does not tell anything about the problem
    #set_similar does not apply
    #set_congruent applies to shapes, not areas
    #set_tan does not apply


def know_ar4():
    if equal_predicate.has('ar4', 'ar3') and equal_predicate.has('a1', 'a2') and tan_predicate.has('s3', 'arc3'):
        set_equal('s2', 's4')
    elif equal_predicate.has('ar4', 'ar3') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4'):
        set_equal('a1', 'a2')
    elif equal_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4') and equal_predicate.has('ar4', 'ar3'):
        set_tan('s3', 'arc3')

def know_ar5():
    if equal_predicate.has('ar5', 'ar2') and equal_predicate.has('arc1', 'arc4'):
        set_equal('s1', 's5')
    elif equal_predicate.has('ar5', 'ar2') and equal_predicate.has('s1', 's5'):
        set_equal('arc1', 'arc4')

def know_ar6():
    print("ar6 known, but undefined")


def know_arc1():
    #SET EQUAL
    if equal_predicate.has('arc1', 'arc4') and equal_predicate.has('s1', 's5'):
        set_equal('ar2', 'ar5')
        set_congruent('ar2', 'ar5')
    elif equal_predicate.has('arc1', 'arc4') and equal_predicate.has('ar2', 'ar5'):
        set_equal('s1', 's5')
    #SET FRACTION
    if fraction_predicate.has('arc1', 'arc4') and fraction_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        set_similar('s1', 's5')
    elif fraction_predicate.has('arc1', 'arc4') and similar_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        set_fraction('s1', 's5', fraction_predicate.get_fraction('arc1', 'arc4'))

    #set sum value #does not tell anything about any other portion of the problem

def know_arc3():
    #### Is ar4 == ar3 necessary?
    if tan_predicate.has('arc3', 's3') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        set_equal('ar4', 'ar3')
        set_congruent('ar4', 'ar3')
    elif tan_predicate.has('arc3', 's3') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar3'):
        set_equal('s2', 's4')
    elif tan_predicate.has('arc3', 's3') and equal_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
         set_equal('a1', 'a2')

    #This one concerns 2
    if fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('s6', 's4')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_fraction('s3', 's7', '2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar3', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('s6', 's2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_fraction('s3', 's7', '2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s6', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('s7', 's4')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.get_fraction('arc3', 'arc5'):
        set_fraction('s3', 's6', '2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar3', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('s7', 's2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2':
        set_fraction('s3', 's6', '2')
    elif fraction_predicate.has('arc3', 'arc5') and equal_predicate.has('s7', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's6') and fraction_predicate.get_fraction('arc3', 'arc5') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2':
        set_equal('a1', 'a2')


def know_arc4():
    if equal_predicate.has('arc4', 'arc1') and equal_predicate.has('s1', 's5'):
        set_equal('ar2', 'ar5')
        set_congruent('ar2', 'ar5')
    elif equal_predicate.has('arc4', 'arc1') and equal_predicate.has('ar2', 'ar5'):
        set_equal('s1', 's5')
    #SET FRACTION
    if fraction_predicate.has('arc4', 'arc1') and fraction_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        set_similar('s1', 's5')
    elif fraction_predicate.has('arc4', 'arc1') and similar_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        set_fraction('s1', 's5', fraction_predicate.get_fraction('arc4', 'arc1'))


def know_arc5():
    #This one concerns 2
    if fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('s6', 's4')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_fraction('s3', 's7', '2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar3', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('ar6', 'ar4')
        set_congruent('ar4', 'ar4')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('s6', 's2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_fraction('s3', 's7', '2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s6', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's7') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's7') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('ar6', 'ar3')
        set_congruent('ar6', 'ar3')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('s7', 's4')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar6', 'ar4') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_fraction('s3', 's6', '2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar3', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('a1', 'a2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('ar6', 'ar4')
        set_congruent('ar6', 'ar4')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('s7', 's2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_fraction('s3', 's6', '2')
    elif fraction_predicate.has('arc5', 'arc3') and equal_predicate.has('s7', 's2') and equal_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's6')  and fraction_predicate.get_fraction('arc5', 'arc3') == '2' and fraction_predicate.get_fraction('s3', 's6') == '2' and not (perpendicular_predicate.has('s2', 's3') or perpendicular_predicate.has('s3', 's4')):
        set_equal('a1', 'a2')


def create_dictionary(predicates):
    dict = {"null" : "NULL"}

    if len(parallel_predicate.relationships) > 0 :
        dict['parallel'] = parallel_predicate.relationships
    if len(perpendicular_predicate.relationships) > 0 :
        dict['perpendicular'] = perpendicular_predicate.relationships
    if len(equal_predicate.relationships) > 0:
        dict['equal'] = equal_predicate.relationships
    if len(fraction_predicate.relationships) > 0:
        dict['fraction'] = fraction_predicate.relationships
    if len(sum_value_predicate.relationships) > 0:
        dict['sum_value'] = sum_value_predicate.relationships
    if len(similar_predicate.relationships) > 0:
        dict['similar'] = similar_predicate.relationships
    if len(congruent_predicate.relationships) > 0:
        dict['congruent'] = congruent_predicate.relationships
    if len(tan_predicate.relationships) > 0:
        dict['tangent'] = tan_predicate.relationships

    if len(dict) > 1:
        dict.pop('null')

    return dict

def remove(predicate_list, A, B):
    new_predicates = []

    for predicate in predicate_list:
        if (predicate[0] == A and predicate[1] == B) or (predicate[0] == B and predicate[1] == A):
            continue
        else:
            new_predicates.append(predicate)

    return new_predicates

def remove_input_predicates(predicates):
    for predicate in predicates:
        if predicate[0] == 'set_parallel':
            if parallel_predicate.has(predicate[1][0], predicate[1][1]):
                parallel_predicate.relationships = remove(parallel_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_perpendicular':
            if perpendicular_predicate.has(predicate[1][0], predicate[1][1]):
                perpendicular_predicate.relationships = remove(perpendicular_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_equal':
            if equal_predicate.has(predicate[1][0], predicate[1][1]):
                equal_predicate.relationships = remove(equal_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_fraction':
            if fraction_predicate.has(predicate[1][0], predicate[1][1]):
                fraction_predicate.relationships = remove(fraction_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_sum_value':
            if sum_value_predicate.has(predicate[1][0], predicate[1][1]):
                sum_value_predicate.relationships = remove(sum_value_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_congruent':
            if congruent_predicate.has(predicate[1][0], predicate[1][1]):
                congruent_predicate.relationships = remove(congruent_predicate.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_tan':
            if tan_predicate.has(predicate[1][0], predicate[1][1]):
                tan_predicate.relationships = remove(tan_predicate.relationships, predicate[1][0], predicate[1][1])
        else:
            print("There was an error with the predicate %s\n" % predicate[0])

def get_all(predicates):

    print("NOTE: FOR THIS PROBLEM, THE ASSUMPTION IS HELD THAT S3 BEING TANGENT TO ARC3\n")
    print("CREATES A BISECTOR OF ARC3")
    for predicate in predicates:
        if predicate[0] == 'set_parallel':
            print("Parallel is not applicable to this problem.\n")
        elif predicate[0] == 'set_perpendicular':
            print(predicate[0])
            set_perpendicular(predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_equal':
            print(predicate[0])
            set_equal(predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_fraction':
            print(predicate[0])
            set_fraction(predicate[1][0], predicate[1][1], predicate[1][2])
        elif predicate[0] == 'set_sum_value':
            print(predicate[0])
            set_sum_value(predicate[1][0], predicate[1][1], predicate[1][2])
        elif predicate[0] == 'set_congruent':
            print(predicate[0])
            print("Congruent is not a valid input for this problem")
        elif predicate[0] == 'set_tan':
            print(predicate[0])
            set_tan(predicate[1][0], predicate[1][1])
        else:
            print("There was an error with the predicate %s\n" % predicate[0])

    remove_input_predicates(predicates)
    dict = create_dictionary(predicates)
    return dict


def solver_problem_2(predicates):
    dict_response = None
    available_variables = ['s1','s2','s3','s4','s5','s6','s7', 'a1','a2', 'a3','ar1','ar2','ar3','ar4','ar5','ar6','arc1','arc3','arc4','arc5','1/n', 'n']
    #verified = verify_user_input(available_variables, predicates)
    #if ( not verified ):
    #    print("Error! The problem variables must come from the same diagram. Refer to the diagrams for exact naming.\n")
    #    return -1

    reset_predicates()
    print("Input Predicates: ")
    print(predicates)
    print("\n")
    set_tan('s3', 'arc3')
    dict_response = get_all(predicates)
    print('Output Predicates: ')
    for k, v in dict_response.items():
        print(k, v)
    print("\n")

def run_test():
    selection = ['side_var', 'angle_var', 'arc_var']
    side_var = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
    angle_var = ['a1', 'a2', 'a3']
    arc_var = ['arc1', 'arc3', 'arc4', 'arc5']
    area_var = ['ar1', 'ar2', 'ar3', 'ar4', 'ar5', 'ar6']
    predicates = ['set_parallel', 'set_perpendicular', 'set_equal', 'set_fraction', 'set_sum_value', 'set_tan']
    sum_value_int = '90'

    amount_of_predicates = random.randint(1,4)
    test = []

    for i in range(amount_of_predicates):
        predicate = predicates[random.randint(0,5)]
        if predicate == 'set_sum_value':
            p1 = angle_var[random.randint(0,2)]
            p2 = angle_var[random.randint(0,2)]
            while p1 == p2:
                p2 = angle_var[random.randint(0,2)]
            test.append([predicate,[p1,p2,sum_value_int]])
            continue
        elif predicate == 'set_perpendicular':
            p1 = side_var[random.randint(0,6)]
            p2 = side_var[random.randint(0,6)]
            while p1 == p2:
                p2 = side_var[random.randint(0,2)]
        elif predicate == 'set_equal':
            select = selection[random.randint(0,2)]
            if select == 'side_var':
                p1 = side_var[random.randint(0,6)]
                p2 = side_var[random.randint(0,6)]
                while p1 == p2:
                    p2 = side_var[random.randint(0,2)]
            elif select == 'angle_var':
                p1 = angle_var[random.randint(0,2)]
                p2 = angle_var[random.randint(0,2)]
                while p1 == p2:
                    p2 = angle_var[random.randint(0,2)]
            elif select == 'arc_var':
                p1 = arc_var[random.randint(0,3)]
                p2 = arc_var[random.randint(0,3)]
                while p1 == p2:
                    p2 = arc_var[random.randint(0,3)]
        elif predicate == 'set_fraction':
            select = selection[random.randint(0,2)]
            if select == 'side_var':
                p1 = side_var[random.randint(0,6)]
                p2 = side_var[random.randint(0,6)]
                while p1 == p2:
                    p2 = side_var[random.randint(0,6)]
            elif select == 'angle_var':
                p1 = angle_var[random.randint(0,2)]
                p2 = angle_var[random.randint(0,2)]
                while p1 == p2:
                    p2 = angle_var[random.randint(0,2)]
            elif select == 'arc_var':
                p1 = arc_var[random.randint(0,3)]
                p2 = arc_var[random.randint(0,3)]
                while p1 == p2:
                    p2 = arc_var[random.randint(0,3)]
            test.append([predicate,[p1,p2,'2']])
            continue
        elif predicate == 'set_tan':
            p1 = 's3'
            p2 = 'arc3'
        elif predicate == 'set_parallel':
            continue
        if not([predicate, [p1, p2]] in test):
            test.append([predicate, [p1, p2]])

    print("Running Test...\n")
    print("Test Input: ")
    print(test)
    print('\n')
    solver_problem_2(test)
