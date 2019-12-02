#!/usr/bin/env python

testdict = {
    "NULL": ["NULL"]
    }
outputdict = dict(testdict)


#starting with line and triangle

class parallel:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_parallel(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships: 
            return True
        else:
            return False

class perpendicular:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_perpendicular(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True
        else:
            return False

#equal being used as a descriptor of length, angle or area
class equal:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_equal(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True        
        else:
          return False


class fraction:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_fraction(self, a, b, fraction):
        self.relationships.append([a,b,fraction])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True
        else:
            return False

class sum_value:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_sum_value(self, a, b, sum):
        self.relationships.append([a,b,sum])

    def has(self, a, b):
        if [a,b] in self.relationships or [a,b] in self.relationships:
            return True
        else:
            return False

class similar:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_similar(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True
        else:
            return False

class congruent:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_congruent(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True
        else:
            return False


class tan:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_tan(self, a, b):
        self.relationships.append([a,b])

    def has(self, a, b):
        if [a,b] in self.relationships or [b,a] in self.relationships:
            return True
        else:
            return False


#actual object instanciation
parallel = parallel()
perpendicular = perpendicular()
equal = equal()
fraction = fraction()
sum_value = sum_value()
similar = similar()
congruent = congruent()
tan = tan()

def set_parallel(name1, name2): #When a “parallel” predicate is given
    if parallel.has(name1, name2):
        return False

    parallel.make_parallel(name1, name2)#calls function that actually makes them parallel

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

def set_perpendicular(name1, name2): #When a “perpendicular” predicate is given
    if perpendicular.has(name1, name2):
        return False

    perpendicular.make_perpendicular(name1, name2)#calls function that actually makes them perpendicular

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
    if equal.has(name1, name2):
        return False
    
    equal.make_equal(name1, name2)#calls function that actually makes them parallel

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
    elif name1 is "ar7":
        know_ar7()       
    elif name1 is "a4":
        know_a4()    
    elif name1 is "a5":
        know_a5()    
    elif name1 is "a6":
        know_a6()    
    elif name1 is "ar7":
        know_a7()    
    elif name1 is "a8":
        know_a8()     


    if name2 is "s8":
        know_s8()
    elif name2 is "s9":
        know_s9()    
    elif name2 is "s10":
        know_s10()   
    elif name2 is "s11":
        know_s11()
    elif name2 is "ar7":
        know_ar7()       
    elif name2 is "a4":
        know_a4()    
    elif name2 is "a5":
        know_a5()    
    elif name2 is "a6":
        know_a6()    
    elif name2 is "ar7":
        know_a7()    
    elif name2 is "a8":
        know_a8()     



def set_fraction(name1, name2,fraction): #When a “parallel” predicate is given
    if fraction.has(name1, name2):
        return False

    fraction.make_fraction(name1, name2, fraction)#calls function that actually makes them parallel

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
    elif name1 is "ar7":
        know_ar7()       
    elif name1 is "a4":
        know_a4()    
    elif name1 is "a5":
        know_a5()    
    elif name1 is "a6":
        know_a6()    
    elif name1 is "ar7":
        know_a7()    
    elif name1 is "a8":
        know_a8()     


    if name2 is "s8":
        know_s8()
    elif name2 is "s9":
        know_s9()    
    elif name2 is "s10":
        know_s10()   
    elif name2 is "s11":
        know_s11()
    elif name2 is "ar7":
        know_ar7()       
    elif name2 is "a4":
        know_a4()    
    elif name2 is "a5":
        know_a5()    
    elif name2 is "a6":
        know_a6()    
    elif name2 is "ar7":
        know_a7()    
    elif name2 is "a8":
        know_a8()     


def set_sum_value(name1, name2,sum): #When a “parallel” predicate is given
    if sum_value.has(name1, name2):
        return False

    sum_value.make_sum_value(name1, name2,sum)#calls function that actually makes them parallel

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
    elif name1 is "ar7":
        know_ar7()       
    elif name1 is "a4":
        know_a4()    
    elif name1 is "a5":
        know_a5()    
    elif name1 is "a6":
        know_a6()    
    elif name1 is "ar7":
        know_a7()    
    elif name1 is "a8":
        know_a8()     


    if name2 is "s8":
        know_s8()
    elif name2 is "s9":
        know_s9()    
    elif name2 is "s10":
        know_s10()   
    elif name2 is "s11":
        know_s11()
    elif name2 is "ar7":
        know_ar7()       
    elif name2 is "a4":
        know_a4()    
    elif name2 is "a5":
        know_a5()    
    elif name2 is "a6":
        know_a6()    
    elif name2 is "ar7":
        know_a7()    
    elif name2 is "a8":
        know_a8()     



def set_similar(name1, name2): #When a “parallel” predicate is given
    if similar.has(name1, name2):
        return False

    similar.make_similar(name1, name2)#calls function that actually makes them parallel

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

def set_congruent(name1, name2): #When a “parallel” predicate is given
    if congruent.has(name1, name2):
        return False

    congruent.make_congruent(name1, name2)#calls function that actually makes them parallel

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

def set_tan(name1, name2): #When a “parallel” predicate is given
    if tan.has(name1, name2):
        return False

    tan.make_tan(name1, name2)#calls function that actually makes them parallel

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


#some left as skeleton functions for testing, since calling them is mandatory for functionality

def know_s8():
    print ("s8 known, and being tested")
    if parallel.has("s8", "s10"):
       set_equal("a5","a7")           
       set_equal("a8","a6")   

def know_s9():
    print ("s9 known, and being tested")
    if equal.has("s9", "s10"):
       set_equal("a5","a4")           
    if equal.has("s9", "s11"):
       set_equal("a5","a6")  

def know_s10():
    print ("s10 known, and being tested")
    if equal.has("s9", "s10"):
       set_equal("a5","a6")  
    if equal.has("s11", "s10"):
       set_equal("a4","a6")  

def know_s11():
    print ("s11 known, and being tested")
    if equal.has("s9", "s11"):
       set_equal("a5","a6")  
    if equal.has("s11", "s10"):
       set_equal("a4","a6")  

def know_a4():
    print ("a4 known, and being tested" )
    if equal.has("a4", "a5"):
       set_equal("s9","s10")  
    if equal.has("a4", "a6"):
       set_equal("s11","s10")
 

def know_a5():
    print ("a5 known, and being tested" )
    if equal.has("a4", "a5"):
       set_equal("s9","s10")  
    if equal.has("a5", "a6"):
       set_equal("s11","s9")  
    if equal.has("a7","a5"):
        set_parallel("s10","s8")

def know_a6():
    print ("a6 known, and being tested" )
    if equal.has("a6", "a5"):
       set_equal("s9","s11")  
    if equal.has("a4", "a6"):
       set_equal("s11","s10")
    if equal.has("a8","a6"):
        set_parallel("s10","s8")  

def know_a7():
    print ("a7 known, and being tested" )
    if equal.has("a7","a5"):
        set_parallel("s10","s8")

def know_a8():
    print ("a8 known, and being tested" )
    if equal.has("a8","a6"):
        set_parallel("s10","s8")  

def know_ar7():
    print ("ar7 known, but undefined" )




def get_all():
    if len(outputdict) == 1:
        print("NULL")
        return "null"

    #for i in parallel.relationships:
        #loop here using
        #outputdict["parallel"] = [stuff]


    outputdict.pop("NULL") 

    print(outputdict)
    return outputdict
    
    #leftovers
    #testdict = {
    #"parallel": ["s8","s11"],
    #"equal": ["s8","s11"],
    #"fraction": ["a5","a6","1/2"]
    #}
    #mydict = dict(testdict)
    #print(testdict)



#testing main
print("parameter 1 test")
set_parallel("s8","s10")
print("parameter 2 test")
set_equal("s11","s10")
get_all()




# code from the sample to be used as reference

#def know_sb6(): # This will be called when a relation that involves sb6 is discovered
#    if set_parallel.has(sb6, sa7) and not set_equal.has(b1,b3): # First half: “If sb6 and sa7
                                                                #are parallel”
                                                                #The second half is for
                                                                #avoiding infinite recursive
                                                                #call, the following functions
                                                                #will skip this part for
                                                                #simplicity. You should not
                                                                #skip it in your project.

#        set_equal(b1, b3) #Then set b1 and b3 to be equal
#        know.b1() # Call related variables
#        know.b3()

#def know_sa7(): # Similar to know_sb6()
#    if set_parallel.has(sb6, sa7):
#        b1.angle() = b3.angle()
#        know.b1()
#       know.b3()

#def know_b1():
#    if set_equal.has(b1, d5): # If b1 and d5 are equal
#        b1.right_angle = True # Then b1 is a right angle (90 degrees)
#        know_b1() # Invoke itself since we find something new about itself
#    if set_equal.has(b1, b3) and b1.right_angle == True: #If b1=b3 and b1 is 90 degree
#        b3.right_angle = True # Then b3 is 90 degrees as well
#        know_b3()
#    if b1.right_angle == True: # This is an example of a rule not used in our
#                                #calculation but is useful in other input combinations
#        set_perpendicular(sc1, sa1) # If b1 is 90 degrees then two adjacent sides are
#                                    #perpendicular

#def know_b3():
#    if set_equal.has(b1, d5):
#        b1.right_angle = True
#        know_b1()
#    if set_equal.has(b1, b3) and b1.right_angle == True:
#        b3.right_angle = True
#        know_b3()
#    if b3.right_angle == True: # If b3 is a right angle
#        set_perpendicular(sc3, sa3) #sc3 and sa3 are perpendicular
#        set_perpendicular(sc7, sa7) #sc7 and sa7 are perpendicular
#        set_sumvalue(a1, c4, 90) #a1 + c4 = 90 since a1 + c4 + b3 = 180
#        know_sc3()
#        know_sa3()
#        know_sc7()
#        know_sa7()
#        know_a1()
#        know_c4()