#FUNDAMENTAL DATA TYPES

a=20
b=523.4535
print(round(b))
"""
14 DATA TYPES  - 5 FUNDAMENTAL DATA TYPES

ALL FUNDAMENTAL DATA TYPES ARE IMMUTABLE """


#TYPE CASTING

#INTEGER int()

no=99.45

print(int(no))


#FLOAT float()

float(10)

print(float(10))

float(True)

print(float(True))

float(False)

print(float(False))

"""doorno = 10/2

print(doorno)"""


#to avoid this division method so convert to str

doorno = "10/2"

print(doorno)

print(str(doorno))

print(type(doorno))



#COMPLEX complex()

print(complex(10))

print(complex(5.4))

print(complex(True))

print(complex(False))

print(complex("12"))

print(complex("12.7"))

print(complex(10,20))

print(complex(True,False))


#BOOLEAN bool()

print(bool(0))

print(bool(1))

print(bool(1.5))

print(bool(0.3))

print(bool(0.0))

print(bool(5+4j))

print(bool(0+2j))

print(bool(0+0j))

print(bool("abc"))

print(bool(""))

print(bool(True))

print(bool(False))


#STRING str()

print(str(10))

#print("price of a tea is" + 10)
#Type Error: must be str not int,

print("price of a tea is" +" " +str(10))

print(str(34.5))

print(str(5+10j))

print(str(True))

print(str(False))

print(str("deepi"))


#immutability

no= 10

print(id(no))

no2 =10

print(id(no2))

no2 =20

print(id(no2))

#IMMUTABILITY

""" Once we change value of an identifier belongs to fundamental data types it wont get changed in memory. Instead of that, a new memory location will be created and the new line will be updated there"""

no1= 10
print(id(no1))

no2= 10.0
print(id(no2))


print(no1 is no2)   #equality          #interview question : diff b/w is and ==  ?#            #IS means rendu memory function nu onna nu pakarathu#

print(no1 == no2)   #identity operator

print(no1 is not no2)


#1 BYTES - 8 Bit  2 power 8

#2*2*2*2*2*2*2*2*2 = 256 bits

"""Group of byte numbers"""

values = [90, 80, 70, 60, 67]

values = bytes(values)

print(type(values))

print(values)

#print(values) #--------> ipadi kudutha random values ah varum  eg: b'ZPF<C' so athuku mela iruka mathiri type casting panni than kudukanum

print(values[0])      

print(values[1])

print(values[2])

print(values[3])

print(values[4])

print(values[-4])

 # another method using LOOP method (unknown values "for" loop use pannanum)


total = 0
for i in values:
    print(i)
    total = total + i
print(total)








