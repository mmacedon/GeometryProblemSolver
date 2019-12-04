#!/usr/bin/env python
from helperfunctions import *
#Circle and triangle

#Prependicular is ommitted since there are no possible ways to
#make perpendicular lines in the Circle and Triangle Problem

class perpendicular:
    def __init__(self):
        self.relationships = []

    def make_perpendicular(self, a, b):
        if [a, b] in self.relationships or [b,a] in self.relationships:
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
            self.relationships.append([a,b,n])

    def has(self, a, b, n):
        if [a, b, n] in self.relationships or [b, a, n] in self.relationships:
            return True
        else:
            return False

class sum_value:
    def __init__(self):
        self.relationships = []

    def make_sum_value(self, a, b, n):
        if [a, b, n] in self.relationships or [b, a, n] in self.relationships:
            return
        else:
            relationships.append([a,b, n])

    def has(self, a, b):
        if [a, b, n] in self.relationships or [a, b, n] in self.relationships:
            return True
        else:
            return False

class similar:
    def __init__(self):
        self.relationships = []

    def make_similar(self, a, b):
        if [a, b] in self.relationships or [b, a] in self.relationships:
            return
        else:
            relationships.append([a,b])

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
            relationships.append([a,b])

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
            relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b, a] in self.relationships:
            return True
        else:
            return False


#actual object instanciation
perpendicular_predicate = perpendicular()
equal_predicate = equal()
fraction_predicate = fraction()
sum_predicate = sum_value()
similar_predicate = similar()
congruent_predicate = congruent()
tan_predicate = tan()

#DEF CHECK_EQUAL_FRACTION_PREDICATES

def set_parallel(name1, name2): #When a “parallel” predicate is given
    if parallel_predicate.has(name1, name2):
        return False

    parallel_predicate.make_parallel(name1, name2)#calls function that actually makes them parallel
    print("\nInputs: %s %s\n" % (name1, name2))

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()

def set_perpendicular(name1, name2): #When a “perpendicular” predicate is given
    if perpendicular_predicate.has(name1, name2):
        return False

    perpendicular_predicate.make_perpendicular(name1, name2)#calls function that actually makes them perpendicular
    print("\nInputs: %s %s\n" % (name1, name2))
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()

def set_equal(name1, name2): #Similar to above
    if equal_predicate.has(name1, name2):
        return False

    equal_predicate.make_equal(name1, name2)#calls function that actually makes them parallel
    print("\nInputs: %s %s\n" % (name1, name2))
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()


def set_fraction(name1, name2,fraction): #When a “parallel” predicate is given
    if fraction_predicate.has(name1, name2):
        return False
    fraction_predicate.make_fraction(name1, name2, fraction)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()

def set_sum_value(name1, name2,sum): #When a “parallel” predicate is given
    if sum_predicate.has(name1, name2):
        return False

    sum_value_predicate.make_sum_value(name1, name2,sum)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()

def set_similar(name1, name2): #When a “parallel” predicate is given
    if similar_predicate.has(name1, name2):
        return False
    similar_predicate.make_similar(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()


def set_congruent(name1, name2): #When a “parallel” predicate is given

    if congruent_predicate.has(name1, name2):
        return False

    congruent_predicate.make_congruent(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later

    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()

def set_tan(name1, name2): #When a “parallel” predicate is given
    if tan_predicate.has(name1, name2):
        return False

    tan_predicate.make_tan(name1, name2)#calls function that actually makes them parallel
    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later

    print("\nInputs: %s %s\n" % (name1, name2))
    if name1 is 's1':
        know_s1()
    elif name1 is 's2':
        know_s2()
    elif name1 is 's3':
        know_s3()
    elif name1 is 's4':
        know_s4()
    elif name1 is 's5':
        know_s5()
    elif name1 is 's6':
        know_s6()
    elif name1 is 's7':
        know_s7()

    if name2 is 's1':
        know_s1()
    elif name2 is 's2':
        know_s2()
    elif name2 is 's3':
        know_s3()
    elif name2 is 's4':
        know_s4()
    elif name2 is 's5':
        know_s5()
    elif name2 is 's6':
        know_s6()
    elif name2 is 's7':
        know_s7()





#some left as skeleton functions for testing, since calling them is mandatory for functionality
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
        for relation in equal_predicate:
            if name1 in relation:
                continue
            if name2 == relation[0] or name2 == relation[1]:
                new = relation[0] if name2 == relation[1] else relation[1]
                if not [name1, new] in equal_predicate and not [new, name1] in equal_predicate:
                   equal_predicate.append([name1, new])

def check_fractional_predicates(name1):
    names = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
    for name2 in names:
        if not [name1, name2] in fraction_predicate and not [name2, name1] in fraction_predicate:
            continue
        if name1 == name2:
            continue
        for relation in equal_predicate:
            if name1 in relation:
                continue
            if name2 == relation[0] or name2 == relation[1]:
                new = relation[0] if name2 == relation[1] else relation[1]
                if not [name1, new] in fraction_predicate and not [new, name1] in fraction_predicate:
                   fraction_predicate.append([name1, new])

def check_similarities():
    #Only 3 conditions to check (ar2, ar5) (ar6, ar4) (ar6, ar3), (ar3, ar4)
    if fraction_predicate.has('s1' , 's5', 'n') and fraction_predicate.has('arc1', 'arc4', 'n'):
        similar_predicate.make_similar('ar2', 'ar5')
        know_ar2()
        know_ar5()

    if equal_predicate.has('a1', 'a2') and fraction_predicate.has('s2', 's4', 'n') and tan_predicate.has('s3', 'arc3'):
        similar_predicate.make_similar('ar4', 'ar3')
        know_ar4()
        know_ar3()

    if equal_predicate.has('a1', 'a2') and ((fraction_predicate.has('s7', 's2', 'n') and fraction_predicate.has('s6', 's3', 'n')) or (fraction_predicate.has('s7', 's3', 'n') and fraction_predicate.has('s6', 's2', 'n'))):
        similar_predicate.make_similar('ar4', 'ar6')
        know_ar4()
        know_ar6()

    if equal_predicate.has('a1', 'a2') and ((fraction_predicate.has('s7', 's4', 'n') and fraction_predicate.has('s6', 's3', 'n')) or (fraction_predicate.has('s7', 's3', 'n') and fraction_predicate.has('s6', 's4', 'n'))):
        similar_predicate.make_similar('ar3', 'ar6')
        know_ar3()
        know_ar6()

def know_s1():

    print("s1 known, but undefined")
    #Consider what knowing S1 reveals about the rest of the Problem
    #If S1 is equal to S5 and Arc1 is equal to arc3, then we know ar2 and ar5 are equal
    #Really gotta cover all know cases.
    #This is gonna be a long night

    #SET EQUAL PREDICATE
    if equal_predicate.has('s1', 's5') and equal_predicate.has('arc1, arc4'):
        congruent_predicate.make_congruent('ar2','ar5')
        know_ar2()
        know_ar5()
    elif equal_predicate.has('s1', 's5') and congruent_predicate.has('ar2','ar5'):
        equal_predicate.make_equal('arc1','arc4')
        know_arc1()
        know_arc4()

    if equal_predicate.has('s1','s5') and equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4'):
         equal_predicate.make_equal('a1', 'a2')
         know_a2()
         know_a3()
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s6', 's7')
        know_s6()
        know_s7()
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s2', 's4')

    check_equal_predicates('s1')

    #SET FRACTION PREDICATE
    if fraction_predicate('s1', 's2'):
        fraction_predicate.make_fraction('s1', 's4')
        know_s4()
    elif fraction_predicate('s1', 's4'):
        fraction_predicate.make_fraction('s1', 's2')
        know_s2()

    if fraction_predicate.has('s1', 'arc1') and congruent_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('s5', 'arc4')
        know_s5()
        know_arc4()
    elif fraction_predicate.has('s1', 's5') and congruent_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('arc1', 'arc4')
        know_arc1()
        know_arc4()
    elif fraction_predicate.has('s1', 'arc4') and congruent_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('s5', 'arc1')
        know_s5()
        know_arc1()
    #EXHAUST ALL THE FRACTION COMBINATIONS
    check_fractional_predicates('s1')

    #SET SUM VALUE #SKIP FOR NOW #Relationship does not tell you anything new about the problem
    #MAY SKIP? WE'LL SEE


def know_s2():
    print("s2 known, but undefined")

    #SET_PERPENDICULAR
    if perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4') and not perpendicular_predicate.has('s7', 's6'):
        sum_value_predicate.make_sum_value('a2', 'a3', '90')
        know_a2()
        know_a3()

    #SET_EQUAL
    if equal_predicate.has('s2', 's4') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s7', 's6')
        know_s7()
        know_s6()
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('s7', 's6') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s2', 's4') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s4', 's7') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s4', 's7')
        know_s4()
        know_s7()
    elif equal_predicate.has('s2', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's7'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    if equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar3', 'ar4')
        know_ar3()
        know_ar4()
    elif equal_predicate.has('s2', 's4') and congruent_predicate.has('ar3', 'ar4') and equal_predicate.has('a1', 'a2'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('s2', 's4') and congruent_predicate.has('ar3', 'ar4') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    check_equal_predicates('s2')


    #No way I can think of if S2 is equal to S3 or S2 equal to S1 or S5.
    #Don't learn anything new

    #SET FRACTION #A = B * n
    ## Double check this one
    if fraction_predicate.has('s3', 's2') and equal_predicate.has('a1', 'a2') and congruent.has('ar4', 'ar3'):
        fraction_predicate.make_fraction('s3', 's4')
        know_s3()
        know_s4()
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and congruent.has('ar3', 'ar4'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    if fraction_predicate.has('s1', 's2') and congruent_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        fraction_predicate.make_fraction('s5', 's2')
        know_s5()
        know_s2()
    elif fraction_predicate.has('s5', 's2') and congruent_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        fraction_predicate.make_fraction('s1', 's2')
        know_s1()
        know_s2()

    if fraction_predicate.has('s2', 's3') and congruent_predicate.has('ar4', 'ar3'):
        fraction_predicate.make_fraction('s3', 's4')
        know_s3()
        know_s4()
    elif fraction_predicate.has('s2', 's3') and fraction_predicate.has('s3', 's4') and equal.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif fraction_predicate.has('s3', 's2') and fraction_predicate.has('s3', 's4') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('a1', 'a3')
        know_a1()
        know_a3()
    check_fractional_predicates('s2')
#EXHAUSTED ALL THE POSSIBLE COMBINATIONS I CAN THINK OF

#KNOWING SUM VALUE DOES NOT PRODUCE ANYTHING NEW THAT I CAN THINK OF OR USEFUL INFORMATION
#SET SIMILAR SCRAPPED
#CONGRUENT: LINES CANNOT BE congruent
#S2 CANNOT BE SET TANGENT. AT LEAST I DON'T THINK, LET'S AWAIT WHAT THE TA SAYS


def know_s3():
    print("s3 known, but undefined")
    #SET PARALLEL DOES NOT APPLY
    #SET perpendicular
    if perpendicular_predicate.has('s3', 's2') and not perpendicular.has('s3', 's4') and not perpendicular_predicate.has('s7', 's6'):
        sum_value_predicate.make_sum_value('a2', 'a3', '90')
        know_a2()
        know_a3()
    elif perpendicular.has('s3', 's4') and not perpendicular_predicate.has('s3', 's2') and not perpendicular_predicate.has('s7', 's6'):
        sum_value_predicate.make_sum_value('a1', 'a3', '90')
        know_a1()
        know_a3()
    #set EQUAL #not sure how this can be done
    #SET tangent
    if tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif tan_predicate.has('s3', 'arc3') and equal_predicate.has('s2', 's4') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar3', 'ar4'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    #SET_FRACTION
    if fraction_predicate.has('s3', 's2') and equal_predicate.has('s2', 's4'):
        fraction_predicate.make_fraction('s3', 's4')
        know_s3()
        know_s4()
    elif fraction_predicate.has('s3', 's4') and equal_predicate.has('s2', 's4'):
        fraction_predicate.make_fraction('s3','s2')
        know_s3()
        know_s2()

    #CAN THE SIDE S3 BE SMALLER THAN ANY OTHER SIDE S, OR MUST IT BE THE BIGGEST
    #SINCE IT IS A STAND ALONE SIDE
    #SET SUM VALUE DOES NOT TELL ANYTHING INTERESTING
    #SET SIMILAR NOT required
    #SET CONGRUENT NOT POSSIBLE FOR LINE S3




def know_s4():
    print("s4 known, but undefined")
    #s4 very similar to s2

    if perpendicular_predicate.has('s4', 's3') and not perpendicular_predicate.has('s3', 's2') and not perpendicular_predicate.has('s7', 's6'):
        sum_value_predicate.make_sum_value('a1', 'a3', '90')
        know_a1()
        know_a3()

    #SET_EQUAL
    if equal_predicate.has('s4', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s7', 's6')
        know_s7()
        know_s6()
    elif equal_predicate.has('s4', 's2') and equal_predicate.has('s7', 's6') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s4', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s2', 's6') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s2', 's6')
        know_s2()
        know_s6()
    elif equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    if equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar3', 'ar4')
        know_ar3()
        know_ar4()
    elif equal_predicate.has('s2', 's4') and congruent_predicate.has('ar3', 'ar4') and equal_predicate.has('a1', 'a2'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('s2', 's4') and congruent_predicate.has('ar3', 'ar4') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    check_equal_predicates('s4')
    #No way I can think of if S2 is equal to S3 or S2 equal to S1 or S5.
    #Don't learn anything new

    #SET FRACTION #A = B * n
## Double check this one
    if fraction_predicate.has('s3', 's4') and equal_predicate.has('a1', 'a2') and congruent.has('ar4', 'ar3'):
        fraction_predicate.make_fraction('s3', 's2')
        know_s3()
        know_s2()
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and congruent.has('ar3', 'ar4'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    if fraction_predicate.has('s1', 's4') and congruent_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        fraction_predicate.make_fraction('s5', 's4')
        know_s5()
        know_s4()
    elif fraction_predicate.has('s5', 's4') and congruent_predicate.has('ar2', 'ar5') and equal_predicate.has('arc1', 'arc4'):
        fraction_predicate.make_fraction('s1', 's4')
        know_s1()
        know_s4()
    if fraction_predicate.has('s4', 's3') and congruent_predicate.has('ar4', 'ar3'):
        fraction_predicate.make_fraction('s3', 's2')
        know_s3()
        know_s2()
    elif fraction_predicate.has('s4', 's3') and fraction_predicate.has('s3', 's2') and equal.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif fraction_predicate.has('s3', 's4') and fraction_predicate.has('s3', 's2') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('a1', 'a3')
        know_a1()
        know_a3()

    check_fractional_predicates('s4')

    #SET SUM VALUE DOES NOT TELL US ANYTHING NEW AS AN INPUT FOR lines
    #SET CONGRUENT ONLY FOR AREAS NOT LINES
    #S4 CANNOT BE SET TANGENT IN THIS CASE


def know_s5():
    print("s5 known, but undefined")
    #S5 VERY SIMILAR TO S1

    if equal_predicate.has('s1', 's5') and equal_predicate.has('arc1, arc4'):
        congruent_predicate.make_congruent('ar2','ar5')
        know_ar2()
        know_ar5()
    elif equal_predicate.has('s1', 's5') and congruent_predicate.has('ar2','ar5'):
        equal_predicate.make_equal('arc1','arc4')
        know_arc1()
        know_arc4()

    if equal_predicate.has('s1','s5') and equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4'):
         equal_predicate.make_equal('a1', 'a2')
         know_a1()
         know_a2()
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1'. 'a2'):
        equal_predicate.make_equal('s6', 's7')
        know_s6()
        know_s7()
    elif equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()

    check_equal_predicates('s5')
    #SET FRACTION PREDICATE
    if fraction_predicate('s5', 's2'):
        fraction_predicate.make_fraction('s5', 's4')
        know_s5()
        know_s4()
    elif fraction_predicate('s5', 's4'):
        fraction_predicate.make_fraction('s5', 's2')
        know_s5()
        know_s2()

    if fraction_predicate.has('s5', 'arc5') and equal_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('s1', 'arc1')
        know_s1()
        know_arc1()
    elif fraction_predicate.has('s1', 's5') and congruent_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('arc1', 'arc4')
        know_arc1()
        know_arc4()
    elif fraction_predicate.has('s5', 'arc1') and congruent_predicate.has('ar2', 'ar5'):
        fraction_predicate.make_fraction('s1', 'arc4')
        know_s1()
        know_arc4()
    #EXHAUST ALL THE FRACTION COMBINATIONS
    check_fractional_predicates('s5')


def know_s6():
    print("s1 known, but undefined")
    # s6 cannot be set parallel to any LINES

    #set perpendicular
    if perpendicular_predicate.has('s6', 's7') and not perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4'):
        sum_value_predicate.make_sum_value('a1', 'a2', '90')
        know_a1()
        know_a2()

    #SET EQUAL
    if equal_predicate.has('s6', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s7', 's4')
        know_s7()
        know_s4()
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's7'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('s6', 's7') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    check_equal_predicates('s6')
    #SET FRACTION

    #SET SUM VALUE DOES NOT TELL ANYTHING NEW ABOUT THE SHAPE
    #SET SIMILAR DOES NOT APPLY IN THIS CASE
    #SET CONGRUENT IS NOT POSSIBLE FOR LINES
    if equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and fraction_predicate.has('arc3', 'arc5', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('arc3', 'arc5', '2')
        know_arc3()
        know_arc5()
    elif equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4') and fraction_predicate.has('arc3', 'arc5', '2'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s3()
        know_s7()
    elif equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7', '2') and fraction_predicate.has('arc3', 'arc5', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    if equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7', '2') and fraction_predicate.has('arc3', 'arc5', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('arc3', 'arc5', '2')
        know_arc3()
        know_arc5()
    elif equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5', '2'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s3()
        know_s7()
    elif equal_predicate.has('s6', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5', '2') and fraction_predicate.has('s3', 's7', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    #SET SUM VALUE DOES NOT TELL ANYTHING UNIQUE ABOUT THE LINES
    #SET SIMILAR DOES NOT APPLY TO THIS CASE
    #SET CONGRUENT DOES NOT APPLY IN THIS CASE
    #CANNOT BE SET TAN TO ANYTHING
    check_fractional_predicates('s6')

def know_s7():
    print("s1 known, but undefined")
    # s7 cannot be set parallel to any LINES

    #set perpendicular
    if perpendicular_predicate.has('s7', 's6') and not perpendicular_predicate.has('s2', 's3') and not perpendicular_predicate.has('s3', 's4'):
        sum_value_predicate.make_sum_value('a1', 'a2', '90')
        know_a1()
        know_a2()
    #SET EQUAL
    if equal_predicate.has('s7', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s6', 's4')
        know_s6()
        know_s4()
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s4', 's6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('a1', 'a2'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('s7', 's6') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    check_equal_predicates('s7')
    #SET FRACTION

    #SET SUM VALUE DOES NOT TELL ANYTHING NEW ABOUT THE SHAPE
    #SET SIMILAR DOES NOT APPLY IN THIS CASE
    #SET CONGRUENT IS NOT POSSIBLE FOR LINES
    if equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and fraction_predicate.has('arc3', 'arc5', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('arc3', 'arc5', '2')
        know_arc3()
        know_arc5()
    elif equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4') and fraction_predicate.has('arc3', 'arc5', '2'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s3()
        know_s6()
    elif equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6', '2') and fraction_predicate.has('arc3', 'arc5', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

    if equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6', '2') and fraction_predicate.has('arc3', 'arc5', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('arc3', 'arc5', '2')
        know_arc3()
        know_arc5()
    elif equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5', '2'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s3()
        know_s6()
    elif equal_predicate.has('s7', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('arc3', 'arc5', '2') and fraction_predicate.has('s3', 's6', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    check_fractional_predicates('s7')

    #SET SUM VALUE DOES NOT TELL ANYTHING UNIQUE ABOUT THE LINES
    #SET SIMILAR DOES NOT APPLY TO THIS CASE
    #SET CONGRUENT DOES NOT APPLY IN THIS CASE
    #CANNOT BE SET TAN TO ANYTHING

def know_a1():
    print("a1 known, but undefined")

    #SET EQUAL
    if equal_predicate.has('a1', 'a2'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()

    if equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        equal_predicate.make_equal('s6', 's7')
        know_s6()
        know_s7()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's4') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's4') and equal_predicate.has('s2', 's6'):
        equal_predicate.make_equal('s5', 's7')
        know_s5()
        know_s7()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's6') and equal_predicate.has('s5', 's7'):
        equal_predicate.make_equal('s1', 's4')
        know_s1()
        know_s4()
    elif equal_predicate.make_equal('a1', 'a2') and equal_predicate.has('s5', 's7') and equal_predicate.has('s1', 's4'):
        equal_predicate.make_equal('s2', 's6')
        know_s2()
        know_s6()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s1', 's6') and equal_predicate.has('s2', 's5'):
        equal_predicate.make_equal('s4', 's7')
        know_s4()
        know_s7()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's5') and equal_predicate.has('s4', 's7'):
        equal_predicate.make_equal('s1', 's6')
        know_s1()
        know_s6()
    elif equal_predicate.has('a1', 'a2') and equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's6'):
        equal_predicate.make_equal('s2', 's5')
        know_s2()
        know_s5()
    if equal_predicate.has('a1', 'a2') and equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif equal_predicate.has('a1', 'a2') and tan_predicate.has('s3', 'arc3') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    #SET FRACTION
    if fraction_predicate.has('a1', 'a2', '2') and sum_value_predicate.has('a2', 'a3', '90'):
        fraction_predicate.make_fraction('a1', 'a3', '2')
        equal_predicate.make_equal('a2', 'a3')
        perpendicular_predicate.make_perpendicular('s2', 's3')
        know_a1()
        know_a3()
        know_a2()
        know_s2()
        know_s3()
    elif fraction_predicate.has('a1', 'a3', '2') and sum_value.has('a2', 'a3', '90'):
        fraction_predicate.make_fraction('a1', 'a2', '2')
        equal_predicate.make_equal('a2', 'a3')
        perpendicular_predicate.make_perpendicular('s2', 's3')
        know_a1()
        know_a3()
        know_a2()
        know_s2()
        know_s3()

    #SET SUM VALUE
    if sum_value_predicate.has('a1', 'a2', '90'):
        perpendicular_predicate.make_perpendicular('s6', 's7')
        know_s6()
        know_s7()
    elif sum_value_predicate.has('a1', 'a3', '90'):
        perpendicular_predicate.make_perpendicular('s3', 's4')
        know_s3()
        know_s4()

def know_a2():
    print("a2")
    #SET EQUAL
    if equal_predicate.has('a2', 'a1'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()

    if equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's5') and equal_predicate.has('s2', 's4'):
        equal_predicate.make_equal('s6', 's7')
        know_s6()
        know_s7()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's4') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's5') and equal_predicate.has('s6', 's7'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's4') and equal_predicate.has('s2', 's6'):
        equal_predicate.make_equal('s5', 's7')
        know_s5()
        know_s7()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's6') and equal_predicate.has('s5', 's7'):
        equal_predicate.make_equal('s1', 's4')
        know_s1()
        know_s4()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s5', 's7') and equal_predicate.has('s1', 's4'):
        equal_predicate.make_equal('s2', 's6')
        know_s2()
        know_s6()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s1', 's6') and equal_predicate.has('s2', 's5'):
        equal_predicate.make_equal('s4', 's7')
        know_s4()
        know_s7()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's5') and equal_predicate.has('s4', 's7'):
        equal_predicate.make_equal('s1', 's6')
        know_s1()
        know_s6()
    elif equal_predicate.has('a2', 'a1') and equal_predicate.has('s4', 's7') and equal_predicate.has('s1', 's6'):
        equal_predicate.make_equal('s2', 's5')
        know_s2()
        know_s5()
    if equal_predicate.has('a2', 'a1') and equal_predicate.has('s2', 's4') and tan_predicate.has('s3', 'arc3'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif equal_predicate.has('a2', 'a1') and tan_predicate.has('s3', 'arc3') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif equal_predicate.has('a2', 'a1') and congruent_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
        tan_predicate.has('s3', 'arc3')
        know_s3()
        know_arc3()

    #SET FRACTION
    if fraction_predicate.has('a2', 'a1', '2') and sum_value_predicate.has('a1', 'a3', '90'):
        fraction_predicate.make_fraction('a2', 'a3', '2')
        equal_predicate.make_equal('a1', 'a3')
        perpendicular_predicate.make_perpendicular('s4', 's3')
        know_a2()
        know_a3()
        know_a1()
        know_s4()
        know_s3()
    elif fraction_predicate.has('a2', 'a3', '2') and sum_value.has('a1', 'a3', '90'):
        fraction_predicate.make_fraction('a2', 'a1', '2')
        equal_predicate.make_equal('a1', 'a3')
        perpendicular_predicate.make_perpendicular('s4', 's3')
        know_a2()
        know_a3()
        know_a1()
        know_s4()
        know_s3()

    #SET SUM VALUE
    if sum_value_predicate.has('a2', 'a1', '90'):
        perpendicular_predicate.make_perpendicular('s6', 's7')
        know_s6()
        know_s7()
    elif sum_value_predicate.has('a2', 'a3', '90'):
        perpendicular_predicate.make_perpendicular('s2', 's3')
        know_s2()
        know_s3()

def know_a3():
    print("a3 known, but undefined")

    if equal_predicate.has('a3', 'a1') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's2') and fraction_predicate.has('s6', 's3', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('s7', 's2') and fraction_predicate.has('s6', 's3', '2') and congruent_predicate.has('ar4', 'ar6'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('a3', 'a1') and fraction_predicate.has('s6', 's3', '2') and congruent_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('s7', 's2')
        know_s7()
        know_s2()
    elif equal_predicate.has('a3', 'a1') and congruent_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's2'):
        fraction_predicate.make_fraction('s6', 's3', '2')
        know_s6()
        know_s3()
    elif equal_predicate.has('a3', 'a1') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's2') and fraction_predicate.has('s7', 's3', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif equal_predicate.has('a3', 'a1') and equal_predicate.has('s6', 's2') and fraction_predicate.has('s7', 's3', '2') and congruent_predicate.has('ar4', 'ar6'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('a3', 'a1') and fraction_predicate.has('s7', 's3', '2') and congruent_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('s6', 's2')
        know_s6()
        know_s2()
    elif equal_predicate.has('a3', 'a1') and congruent_predicate.has('ar4', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's2'):
        fraction_predicate.make_fraction('s7', 's3', '2')
        know_s7()
        know_s3()

    if equal_predicate.has('a3', 'a2') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s6', 's3', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s6', 's3', '2') and congruent_predicate.has('ar3', 'ar6'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('a3', 'a2') and fraction_predicate.has('s6', 's3', '2') and congruent_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('s7', 's4')
        know_s7()
        know_s4()
    elif equal_predicate.has('a3', 'a2') and congruent_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s7', 's4'):
        fraction_predicate.make_fraction('s6', 's3', '2')
        know_s6()
        know_s3()
    elif equal_predicate.has('a3', 'a2') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s7', 's3', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif equal_predicate.has('a3', 'a2') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s7', 's3', '2') and congruent_predicate.has('ar3', 'ar6'):
        tan_predicate.make_tan('s3', 'arc3')
        know_s3()
        know_arc3()
    elif equal_predicate.has('a3', 'a2') and fraction_predicate.has('s7', 's3', '2') and congruent_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3'):
        equal_predicate.make_equal('s6', 's4')
        know_s6()
        know_s4()
    elif equal_predicate.has('a3', 'a2') and congruent_predicate.has('ar3', 'ar6') and tan_predicate.has('s3', 'arc3') and equal_predicate.has('s6', 's4'):
        fraction_predicate.make_fraction('s7', 's3', '2')
        know_s7()
        know_s3()


    #SET FRACTION
    if fraction_predicate.has('a3', 'a1', '2') and sum_value_predicate.has('a1', 'a2', '90'):
        fraction_predicate.make_fraction('a3', 'a2', '2')
        equal_predicate.make_equal('a1', 'a2')
        perpendicular_predicate.make_perpendicular('s6', 's7')
        know_a3()
        know_a2()
        know_a1()
        know_s6()
        know_s7()
    elif fraction_predicate.has('a3', 'a2', '2') and sum_value.has('a1', 'a2', '90'):
        fraction_predicate.make_fraction('a3', 'a1', '2')
        equal_predicate.make_equal('a1', 'a2')
        perpendicular_predicate.make_perpendicular('s6', 's7')
        know_a3()
        know_a2()
        know_a1()
        know_s6()
        know_s7()

    #SET SUM_VALUE
    if sum_value_predicate.has('a3', 'a1', '90'):
        perpendicular_predicate.make_perpendicular('s3', 's4')
        know_s3()
        know_s4()
    elif sum_value_predicate.has('a3', 'a2', '90'):
        perpendicular_predicate.make_perpendicular('s2', 's3')
        know_s2()
        know_s3()

def know_ar1():
    print("ar1 known, but undefined")
def know_ar2():
    print("ar2 known, but undefined")
def know_ar3():
    print("ar3 known, but undefined")
def know_ar4():
    print("ar4 known, but undefined")
def know_ar5():
    print("ar5 known, but undefined")
def know_ar6():
    print("ar6 known, but undefined")


def know_arc1():
    print("arc1 known, but undefined")
    #SET EQUAL
    if equal_predicate.has('arc1', 'arc4') and equal_predicate.has('s1', 's5'):
        congruent_predicate.make_congruent('ar2', 'ar5')
        know_ar2()
        know_ar5()

    elif equal_predicate.has('arc1', 'arc4') and congruent_predicate.has('ar2', 'ar5'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()

    #SET FRACTION
    if fraction_predicate.has('arc1', 'arc4', 'n') and fraction_predicate.has('s1', 's5', 'n') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        similar_predicate.make_similar('s1', 's5')
        know_s1()
        know_s5()
    elif fraction_predicate.has('arc1', 'arc4', 'n') and similar_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        fraction_predicate.make_fraction('s1', 's5', 'n')
        know_s1()
        know_s5()
    #set sum value #does not tell anything about any other portion of the problem

def know_arc3():
    print("arc3 known, but undefined")
    if tan_predicate.has('arc3', 's3') and equal_predicate.has('s2', 's4') and equal_predicate.has('a1', 'a2'):
        congruent_predicate.make_congruent('ar4', 'ar3')
        know_ar4()
        know_ar3()
    elif tan_predicate.has('arc3', 's3') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar3'):
        equal_predicate.make_equal('s2', 's4')
        know_s2()
        know_s4()
    elif elif tan_predicate.has('arc3', 's3') and congruent_predicate.has('ar4', 'ar3') and equal_predicate.has('s2', 's4'):
         equal_predicate.make_equal('a1', 'a2')
         know_a1()
         know_a2()

    if fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s6', 's4')
        know_s6()
        know_s4()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s3()
        know_s7()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s6', 's2')
        know_s6()
        know_s2()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s3()
        know_s7()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s6', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's7', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s7', 's4')
        know_s7()
        know_s4()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s6()
        know_s3()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s7', 's2')
        know_s7()
        know_s2()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s3()
        know_s6()
    elif fraction_predicate.has('arc3', 'arc5', '2') and equal_predicate.has('s7', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's6', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

def know_arc4():
    print("arc4 known")
    if equal_predicate.has('arc4', 'arc1') and equal_predicate.has('s1', 's5'):
        congruent_predicate.make_congruent('ar2', 'ar5')
        know_ar2()
        know_ar5()
    elif equal_predicate.has('arc4', 'arc1') and congruent_predicate.has('ar2', 'ar5'):
        equal_predicate.make_equal('s1', 's5')
        know_s1()
        know_s5()
    #SET FRACTION
    if fraction_predicate.has('arc4', 'arc1', 'n') and fraction_predicate.has('s1', 's5', 'n') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        similar_predicate.make_similar('s1', 's5')
        know_s1()
        know_s5()
    elif fraction_predicate.has('arc4', 'arc1', 'n') and similar_predicate.has('s1', 's5') and not (equal.has('s1', 's5') or equal.has('s1', 's5')):
        fraction_predicate.make_fraction('s1', 's5', 'n')
        know_s1()
        know_s5()

def know_arc5():
    print("arc5 known")
    if fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s6', 's4')
        know_s6()
        know_s4()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s3()
        know_s7()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's4') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's7', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's7', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s6', 's2')
        know_s6()
        know_s2()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('s3', 's7', '2')
        know_s7()
        know_s3()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s6', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's7', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2'):
        congruent_predicate.make_congruent('ar6', 'ar3')
        know_ar6()
        know_ar3()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s7', 's4')
        know_s7()
        know_s4()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's4') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar6', 'ar4'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s3()
        know_s6()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's4') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar3', 'ar6'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1' ,'a2') and fraction_predicate.has('s3', 's6', '2'):
        congruent_predicate.make_congruent('ar6', 'ar4')
        know_ar6()
        know_ar4()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('a1', 'a2') and fraction_predicate.has('s3', 's6', '2') and congruent_predicate.has('ar4', 'ar6'):
        equal_predicate.make_equal('s7', 's2')
        know_s7()
        know_s2()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's2') and equal_predicate.has('a1', 'a2') and congruent_predicate.has('ar4', 'ar6'):
        fraction_predicate.make_fraction('s3', 's6', '2')
        know_s3()
        know_s6()
    elif fraction_predicate.has('arc5', 'arc3', '2') and equal_predicate.has('s7', 's2') and congruent_predicate.has('ar4', 'ar6') and fraction_predicate.has('s3', 's6', '2'):
        equal_predicate.make_equal('a1', 'a2')
        know_a1()
        know_a2()

def get_all(predicates):

    print("NOTE: FOR THIS PROBLEM, THE ASSUMPTION IS HELD THAT S3 BEING TANGENT TO ARC3\N")
    print("CREATES A BISECTOR OF ARC3")
    for predicate in predicates:
        if predicate[0] == 'set_parallel':
            print("Parallel is not applicable to this problem.\n")
        elif predicate[0] == 'set_perpendicular':
            set_perpendicular(predicate[1][0], predicate[1][0])
        elif predicate[0] == 'set_equal':
            set_equal(predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_fraction':
            set_fraction(predicate[1][0], predicate[1][1], predicate[1][2])
        elif predicate[0] == 'set_sum_value':
            set_sum_value(predicate[1][0], predicate[1][1], predicate[1][2])
        elif predicate[0] == 'set_congruent':
            set_congruent(predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_tangent':
            set_tanget(predicate[1][0], predicate[1][1])
        else:
            print("There was an error with the predicate %s\n" % predicate[0])

    testdict = {
    "parallel": ["s8","s11"],
    "equal": ["s8","s11"],
    "fraction": ["a5","a6","1/2"]
    }
    mydict = dict(testdict)
    print(testdict)
    return mydict


    #else:
    return "null"

def solver_problem_2(predicates):
    dict_reponse = None
    available_variables = ['s1','s2','s3','s4','s5','s6','s7', 'a1','a2', 'a3','ar1','ar2','ar3','ar4','ar5','ar6','arc1','arc3','arc4','arc5','1/n', 'n']
    verified = verify_user_input(available_variables, predicates)
    if ( not verified ):
        print("Error! The problem variables must come from the same diagram. Refer to the diagrams for exact naming.\n")
        return -1

    dict_response = get_all(predicates)
    return dict_response
