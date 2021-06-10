# import functions
#
# functions.simpleSum(1, 2)

###################
# from functions import simpleSum
#
# simpleSum(1, 2)

##################
# from functions import  *
#
# simpleSum(1, 2)

#################
# from functions import simpleSum as somma
#
# somma(1, 2)
##################
from libreriaTest import testF, testF2, Veicolo, Automobile

testF()
testF2("ciao")

v = Veicolo("xxxxxx")
v.printTarga()
# v.printSottocategoria()  # Errore!!!
print(Veicolo.counter)
print(type(v))
print(isinstance(v, Automobile))
print(isinstance(v, Veicolo))

a = Automobile('yyyyyyy', "furgone")
a.printTarga()
a.printSottocategoria()
print(Veicolo.counter)
print(type(a))
print(isinstance(a, Automobile))
print(isinstance(a, Veicolo))
