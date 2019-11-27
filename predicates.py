#!/usr/bin/env python



#starting with line and triangle

class parallel:
    def __init__():
        self.relationships = []

    def make_parallel(self, a, b):
        relationships.append([a,b])


class equal:
    def __init__():
        self.relationships = []

    def make_equal(self, a, b):
        relationships.append([a,b])

#actual object instanciation
set_parallel = parallel()
set_equal = equal()

def set_parallel(name1, name2): #When a “parallel” predicate is given
    set_parallel.make_parallel(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 is "s8":  
        know_s8()
    elif name1 is "s9":
        know_s9()    
    elif name1 is "s10":
        know_s10()   
    elif name1 is "s11":
        know_s11()

    if name2 is "s8":
        know_s8()
    elif name2 is "s9":
        know_s9()    
    elif name2 is "s10":
        know_s10()   
    elif name2 is "s11":
        know_s11()

def set_equal(name1, name2): #Similar to above
    call: know_name1()
    call: know_name2()

def know_sb6(): # This will be called when a relation that involves sb6 is discovered
    if set_parallel.has(sb6, sa7) and not set_equal.has(b1,b3): # First half: “If sb6 and sa7
                                                                #are parallel”
                                                                #The second half is for
                                                                #avoiding infinite recursive
                                                                #call, the following functions
                                                                #will skip this part for
                                                                #simplicity. You should not
                                                                #skip it in your project.

        set_equal(b1, b3) #Then set b1 and b3 to be equal
        know.b1() # Call related variables
        know.b3()

def know_sa7(): # Similar to know_sb6()
    if set_parallel.has(sb6, sa7):
        b1.angle() = b3.angle()
        know.b1()
        know.b3()

def know_b1():
    if set_equal.has(b1, d5): # If b1 and d5 are equal
        b1.right_angle = True # Then b1 is a right angle (90 degrees)
        know_b1() # Invoke itself since we find something new about itself
    if set_equal.has(b1, b3) and b1.right_angle == True: #If b1=b3 and b1 is 90 degree
        b3.right_angle = True # Then b3 is 90 degrees as well
        know_b3()
    if b1.right_angle == True: # This is an example of a rule not used in our
                                #calculation but is useful in other input combinations
        set_perpendicular(sc1, sa1) # If b1 is 90 degrees then two adjacent sides are
                                    #perpendicular

def know_b3():
    if set_equal.has(b1, d5):
        b1.right_angle = True
        know_b1()
    if set_equal.has(b1, b3) and b1.right_angle == True:
        b3.right_angle = True
        know_b3()
    if b3.right_angle == True: # If b3 is a right angle
        set_perpendicular(sc3, sa3) #sc3 and sa3 are perpendicular
        set_perpendicular(sc7, sa7) #sc7 and sa7 are perpendicular
        set_sumvalue(a1, c4, 90) #a1 + c4 = 90 since a1 + c4 + b3 = 180
        know_sc3()
        know_sa3()
        know_sc7()
        know_sa7()
        know_a1()
        know_c4()