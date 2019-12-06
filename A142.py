#!/usr/bin/env python
import random

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
        if outputdict.get("parallel") is not None:
            outputdict["parallel"].append([a,b])

        else:
            outputdict["parallel"] = [[a,b]]

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
        if outputdict.get("perpendicular") is not None:
            outputdict["perpendicular"].append([a,b])

        else:
            outputdict["perpendicular"] = [[a,b]]

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
        if outputdict.get("equal") is not None:
            outputdict["equal"].append([a,b])

        else:
            outputdict["equal"] = [[a,b]]

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
        if outputdict.get("fraction") is not None:
            outputdict["fraction"].append([a,b])

        else:
            outputdict["fraction"] = [[a,b]]

    def has(self, a, b,c):
        if [a,b,c] in self.relationships or [b,a,c] in self.relationships:
            return True
        else:
            return False

            return False
            return False

    def get_fraction(self,a,b):
        for i in self.relationships:
            if (i[0] is a and i[1] is b) or (i[0] is a and i[1] is b):
                return i[2]
        return "null"

    #def has(self, a, b):
    #    if [a,b,self.get_fraction(self,a,b)] in self.relationships or [b,a,self.get_fraction(self,a,b)] in self.relationships:
    #        return True
    #    else:
    #        return False



class sum_value:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_sum_value(self, a, b, sum):
        self.relationships.append([a,b,sum])
        if outputdict.get("sum_value") is not None:
            outputdict["sum_value"].append([a,b])

        else:
            outputdict["sum_value"] = [[a,b]]

    def has(self, a, b,c):
        if [a,b,c] in self.relationships or [a,b,c] in self.relationships:
            return True
        else:
            return False

    #def has(self, a, b):
    #    if [a,b,get_sum(self,a,b)] in self.relationships or [b,a,get_sum(self,a,b)] in self.relationships:
    #        return True
    #    else:
    #        return False

    def get_sum(self,a,b):
        for i in self.relationships:
            if (i[0] is a and i[1] is b) or (i[0] is b and i[1] is a):
                return i[2]
        return "null"

class similar:
    relationships = []

    #def __init__(self):
    #    self.relationships = []

    def make_similar(self, a, b):
        self.relationships.append([a,b])
        if outputdict.get("similar") is not None:
            outputdict["similar"].append([a,b])

        else:
            outputdict["similar"] = [[a,b]]

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
        if outputdict.get("congruent") is not None:
            outputdict["congruent"].append([a,b])

        else:
            outputdict["congruent"] = [[a,b]]

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
        if outputdict.get("tangent") is not None:
            outputdict["tangent"].append([a,b])

        else:
            outputdict["tangent"] = [[a,b]]

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
similar = similar() #not needed, only one triangle
congruent = congruent() #not needed, only one triangel
tan = tan() #not needed, no circles

def set_parallel(name1, name2): #When a “parallel” predicate is given
    if parallel.has(name1, name2):
        return False

    parallel.make_parallel(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()

    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()

def set_perpendicular(name1, name2): #When a “perpendicular” predicate is given
    if perpendicular.has(name1, name2):
        return False

    perpendicular.make_perpendicular(name1, name2)#calls function that actually makes them perpendicular

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()

    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()

def set_equal(name1, name2): #Similar to above
    if equal.has(name1, name2):
        return False

    equal.make_equal(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()
    elif name1 == 'ar7':
        know_ar7()
    elif name1 == 'a4':
        know_a4()
    elif name1 == 'a5':
        know_a5()
    elif name1 == 'a6':
        know_a6()
    elif name1 == 'a7':
        know_a7()
    elif name1 == 'a8':
        know_a8()


    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()
    elif name2 == 'ar7':
        know_ar7()
    elif name2 == 'a4':
        know_a4()
    elif name2 == 'a5':
        know_a5()
    elif name2 == 'a6':
        know_a6()
    elif name2 == 'a7':
        know_a7()
    elif name2 == 'a8':
        know_a8()



def set_fraction(name1, name2,fraction): #When a “parallel” predicate is given
    if fraction.has(name1, name2):
        return False

    fraction.make_fraction(name1, name2, fraction)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()
    elif name1 == 'ar7':
        know_ar7()
    elif name1 == 'a4':
        know_a4()
    elif name1 == 'a5':
        know_a5()
    elif name1 == 'a6':
        know_a6()
    elif name1 == 'a7':
        know_a7()
    elif name1 == 'a8':
        know_a8()


    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()
    elif name2 == 'ar7':
        know_ar7()
    elif name2 == 'a4':
        know_a4()
    elif name2 == 'a5':
        know_a5()
    elif name2 == 'a6':
        know_a6()
    elif name2 == 'a7':
        know_a7()
    elif name2 == 'a8':
        know_a8()


def set_sum_value(name1, name2,sum): #When a “parallel” predicate is given
    if sum_value.has(name1, name2, sum):
        return False

    sum_value.make_sum_value(name1, name2,sum)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()
    elif name1 == 'ar7':
        know_ar7()
    elif name1 == 'a4':
        know_a4()
    elif name1 == 'a5':
        know_a5()
    elif name1 == 'a6':
        know_a6()
    elif name1 == 'a7':
        know_a7()
    elif name1 == 'a8':
        know_a8()


    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()
    elif name2 == 'ar7':
        know_ar7()
    elif name2 == 'a4':
        know_a4()
    elif name2 == 'a5':
        know_a5()
    elif name2 == 'a6':
        know_a6()
    elif name2 == 'a7':
        know_a7()
    elif name2 == 'a8':
        know_a8()



def set_similar(name1, name2): #When a “parallel” predicate is given
    if similar.has(name1, name2):
        return False

    similar.make_similar(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()

    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()

def set_congruent(name1, name2): #When a “parallel” predicate is given
    if congruent.has(name1, name2):
        return False

    congruent.make_congruent(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()

    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()

def set_tan(name1, name2): #When a “parallel” predicate is given
    if tan.has(name1, name2):
        return False

    tan.make_tan(name1, name2)#calls function that actually makes them parallel

    #calls corrosponding know functions
    #there has got to be a better way to do this, might make the call know thing a seperate function later
    if name1 == 's8':
        know_s8()
    elif name1 == 's9':
        know_s9()
    elif name1 == 's10':
        know_s10()
    elif name1 == 's11':
        know_s11()

    if name2 == 's8':
        know_s8()
    elif name2 == 's9':
        know_s9()
    elif name2 == 's10':
        know_s10()
    elif name2 == 's11':
        know_s11()


#some left as skeleton functions for testing, since calling them is mandatory for functionality

def know_s8():
    print ("s8 known, and being tested")
    if parallel.has("s8", "s10"):
       set_equal("a5","a7")
       set_equal("a8","a6")
    if parallel.has("s8", "s11"):
       set_sum_value("a4","a8","180")
    if parallel.has("s8", "s9"):
       set_sum_value("a4","a7","180")
    if set_perpendicular("s8","s9"):
        set_sum_value("a4","a7","90")
    if set_perpendicular("s8","s11"):
        set_sum_value("a4","a8","90")



def know_s9():
    print ("s9 known, and being tested")
    if equal.has("s9", "s10"):
       set_equal("a5","a4")
    if equal.has("s9", "s11"):
       set_equal("a5","a6")
    if parallel.has("s8", "s9"):
       set_sum_value("a4","a7","180")
    if set_perpendicular("s8","s9"):
        set_sum_value("a4","a7","90")
    if set_perpendicular("s10","s9"):
        set_sum_value("a4","a5","90")
    if set_perpendicular("s11","s9"):
        set_sum_value("a5","a6","90")

def know_s10():
    print ("s10 known, and being tested")
    if parallel.has("s8", "s10"):
       set_equal("a5","a7")
       set_equal("a8","a6")
    if equal.has("s9", "s10"):
       set_equal("a5","a6")
    if equal.has("s11", "s10"):
       set_equal("a4","a6")
    if set_perpendicular("s10","s9"):
        set_sum_value("a4","a5","90")
    if set_perpendicular("s10","s11"):
        set_sum_value("a4","a6","90")

def know_s11():
    print ("s11 known, and being tested")
    if parallel.has("s8", "s11"):
       set_sum_value("a4","a8","180")
    if set_perpendicular("s8","s11"):
        set_sum_value("a4","a8","90")
    if set_perpendicular("s11","s10"):
        set_sum_value("a4","a6","90")
    if set_perpendicular("s11","s9"):
        set_sum_value("a5","a6","90")
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
    if sum_value.has("a4","a5","90"):
        set_perpendicular("s9","s10")
    if sum_value.has("a4","a6","90"):
        set_perpendicular("s11","s10")

    #if equal.has("a4", "a7"):
    #   set_equal("s11","s10")


def know_a5():
    print ("a5 known, and being tested" )
    if equal.has("a4", "a5"):
       set_equal("s9","s10")
    if equal.has("a5", "a6"):
       set_equal("s11","s9")
    if equal.has("a7","a5"):
        set_parallel("s10","s8")
    if sum_value.has("a4","a5","90"):
        set_perpendicular("s9","s10")
    if sum_value.has("a6","a5","90"):
        set_perpendicular("s11","s9")

def know_a6():
    print ("a6 known, and being tested" )
    if equal.has("a6", "a5"):
       set_equal("s9","s11")
    if equal.has("a4", "a6"):
       set_equal("s11","s10")
    if equal.has("a8","a6"):
        set_parallel("s10","s8")
    if sum_value.has("a6","a5","90"):
        set_perpendicular("s9","s11")
    if sum_value.has("a4","a6","90"):
        set_perpendicular("s11","s10")

def know_a7():
    print ("a7 known, and being tested" )
    if equal.has("a7","a5"):
        set_parallel("s10","s8")
    if sum_value.has("a7","a8",sum_value.get_sum("a7","a8")):
        set_sum_value("a7","a8",sum_value.get_sum("a7","a8"))
    if sum_value.has("a7","a4","180"):
        set_parallel("s8","s9")
    if sum_value.has("a7","a4","90"):
        set_perpendicular("s8","s9")

    #   set_sum_value("a4","a7","180")
    #if set_perpendicular("s8","s9"):
    #    set_sum_value("a4","a7","90")

def know_a8():
    print ("a8 known, and being tested" )
    if equal.has("a8","a6"):
        set_parallel("s10","s8")
    if sum_value.has("a7","a8",sum_value.get_sum("a7","a8")):
        set_sum_value("a7","a8",sum_value.get_sum("a7","a8"))
    if sum_value.has("a8","a4","180"):
        set_parallel("s8","s11")
    if sum_value.has("a8","a4","90"):
        set_perpendicular("s11","s8")

def know_ar7():
    print ("ar7 known, but useless in this problem" )

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
            if parallel.has(predicate[1][0], predicate[1][1]):
                parallel.relationships = remove(parallel.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_perpendicular':
            if perpendicular.has(predicate[1][0], predicate[1][1]):
                perpendicular.relationships = remove(perpendicular.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_equal':
            if equal.has(predicate[1][0], predicate[1][1]):
                equal.relationships = remove(equal.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_fraction':
            if fraction.has(predicate[1][0], predicate[1][1],predicate[1][2]):
                fraction.relationships = remove(fraction.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_sum_value':
            if sum_value.has(predicate[1][0], predicate[1][1],predicate[1][3]):
                sum_value.relationships = remove(sum_value.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_congruent':
            if congruent.has(predicate[1][0], predicate[1][1]):
                congruent.relationships = remove(congruent.relationships, predicate[1][0], predicate[1][1])
        elif predicate[0] == 'set_tan':
            if tan.has(predicate[1][0], predicate[1][1]):
                tan.relationships = remove(tan.relationships, predicate[1][0], predicate[1][1])
        else:
            print("There was an error with the predicate %s\n" % predicate[0])


def create_dictionary(predicates):
    dict = {"null" : "NULL"}

    if len(parallel.relationships) > 0 :
        dict['parallel'] = parallel.relationships
    if len(perpendicular.relationships) > 0 :
        dict['perpendicular'] = perpendicular.relationships
    if len(equal.relationships) > 0:
        dict['equal'] = equal.relationships
    if len(fraction.relationships) > 0:
        dict['fraction'] = fraction.relationships
    if len(sum_value.relationships) > 0:
        dict['sum_value'] = sum_value.relationships
    if len(similar.relationships) > 0:
        dict['similar'] = similar.relationships
    if len(congruent.relationships) > 0:
        dict['congruent'] = congruent.relationships
    if len(tan.relationships) > 0:
        dict['tangent'] = tan.relationships

    if len(dict) > 1:
        dict.pop('null')

    return dict

def get_all(predicates):
    #added in later in development
    for predicate in predicates:
        if predicate[0] == 'set_parallel':
            print(predicate[0])
            set_parallel(predicate[1][0], predicate[1][1])
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
            print("Congruent is not a valid input for this problem")
        else:
            print("There was an error with the predicate %s\n" % predicate[0])


    if len(outputdict) == 1:#check for when dictionary is functionally empty and returns null
        print("NULL")
        return "null"

    #for i in parallel.relationships:
        #loop here using
        #outputdict["parallel"] = [stuff]


    remove_input_predicates(predicates)
    dict = create_dictionary(predicates)
    return dict

    #outputdict.pop("NULL") #removes temporary null from dictionary

    #print(outputdict)
    #return outputdict

    #leftovers
    #testdict = {
    #"parallel": ["s8","s11"],
    #"equal": ["s8","s11"],
    #"fraction": ["a5","a6","1/2"]
    #}
    #mydict = dict(testdict)
    #print(testdict)



#extra functions to interface with the main
#DEF CHECK_EQUAL_FRACTION_PREDICATES
def reset_predicates():
    parallel.relationships = []
    perpendicular.relationships = []
    equal.relationships = []
    fraction.relationships = []
    sum_value.relationships = []
    similar.relationships = []
    congruent.relationships = []
    tan.relationships = []

def solver_problem_1(predicates):
    dict_response = None
    available_variables = ['s8','s9','s10','s11', 'a4','a5', 'a6', 'a7', 'a8','ar7','1/n', 'n']

    reset_predicates()
    print("Input Predicates: ")
    print(predicates)
    print("\n")
    dict_response = get_all(predicates)
    print('Output Predicates: ')
    for k, v in dict_response.items():
        print(k, v)
    print("\n")

def run_test():
    selection = ['side_var', 'angle_var']
    side_var = ['s8', 's9', 's10', 's11']
    angle_var = ['a4', 'a5', 'a6', 'a7', 'a8']
    #area_var = ['ar7']
    predicates = ['set_parallel', 'set_perpendicular', 'set_equal', 'set_fraction', 'set_sum_value']
    sum_value_int = ['90','180']

    amount_of_predicates = random.randint(1,4)
    test = []

    for i in range(amount_of_predicates):
        predicate = predicates[random.randint(0,5)]
        if predicate == 'set_sum_value':
            p1 = angle_var[random.randint(0,4)]
            p2 = angle_var[random.randint(0,4)]
            s1 = sum_value_int[random.randint(0,1)]
            while p1 == p2:
                p2 = angle_var[random.randint(0,4)]
            test.append([predicate,[p1,p2,s1]])
            continue
        elif predicate == 'set_perpendicular':
            p1 = side_var[random.randint(0,3)]
            p2 = side_var[random.randint(0,3)]
            while p1 == p2:
                p2 = side_var[random.randint(0,3)]
        elif predicate == 'set_equal':
            select = selection[random.randint(0,1)]
            if select == 'side_var':
                p1 = side_var[random.randint(0,3)]
                p2 = side_var[random.randint(0,3)]
                while p1 == p2:
                    p2 = side_var[random.randint(0,3)]
            elif select == 'angle_var':
                p1 = angle_var[random.randint(0,4)]
                p2 = angle_var[random.randint(0,4)]
                while p1 == p2:
                    p2 = angle_var[random.randint(0,4)]
            
        elif predicate == 'set_fraction':
            select = selection[random.randint(0,1)]
            if select == 'side_var':
                p1 = side_var[random.randint(0,3)]
                p2 = side_var[random.randint(0,3)]
                while p1 == p2:
                    p2 = side_var[random.randint(0,3)]
            elif select == 'angle_var':
                p1 = angle_var[random.randint(0,4)]
                p2 = angle_var[random.randint(0,4)]
                while p1 == p2:
                    p2 = angle_var[random.randint(0,4)]
            test.append([predicate,[p1,p2,'2']])
            continue

        elif predicate == 'set_parallel':
            continue
        if not([predicate, [p1, p2]] in test):
            test.append([predicate, [p1, p2]])

    print("Running Test...\n")
    print("Test Input: ")
    print(test)
    print('\n')
    solver_problem_1(test)






#testing main
#print("parameter 1 test")
#set_parallel("s8","s11")
#print("parameter 2 test")
#set_equal("a4","a6")
#print("parameter 3 test")
#set_sum_value("a7","a8","90")
#get_all()




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
