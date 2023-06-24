A = ['N','E','W']
A.sort(reverse = True)
print(A[0])


print('Hello'[0+1+2])


Which is a Set??
(9, 8, 7)
{6, 5, 4}
{'1':'I'}
[3, 2, 1]


pP = ['p','P']
pP.sort()
print(pP[0])

# OUTPUT: P

# EXPLANATION: 
# The code sorts the list `pP` in ascending order 
# and then prints the first element of the sorted list. 
# Since 'P' comes before 'p' in alphabetical order, 
# the OUTPUT will be 'P'.

# OUTPUT AFTER EACH LINE:
pP = ['p', 'P']
print(pP)  # OUTPUT: ['p', 'P']

pP.sort()
print(pP)  # OUTPUT: ['P', 'p']

print(pP[0])  # OUTPUT: P


####################################################################################################

ON = ['N','O']
ON.sort()
for ON in ON:
  print(ON)

# OUTPUT: 
# N
# O

# EXPLANATION: 
# In this code, 
# the list is sorted using the sort() method 
# before iterating over its elements. 
# The loop variable is named ON. 
# Each element of the sorted list 
# is then printed on a separate line.

# OUTPUT AFTER EACH LINE:
ON = ['N','O']
print(ON)  # OUTPUT: ['N', 'O']

ON.sort()
print(ON)  # OUTPUT: ['N', 'O']

for ON in ON:
  print(ON)  
# OUTPUT:
# N
# O


####################################################################################################

X = ['T','O','P']
X.sort()
print(X[0])

# OUTPUT: O

# EXPLANATION: 
# The code will sort the list X in alphabetical order 
# and then print the first element of the sorted list.

# OUTPUT AFTER EACH LINE:
X = ['T','O','P']
print(X)  # OUTPUT: ['T','O','P']

X.sort()
print(X)  # OUTPUT: ['O', 'P', 'T']

print(X[0])  # OUTPUT: O


####################################################################################################

AI = ['T' 'R' 'E' 'N' 'D']
[print(Py) for Py in AI]

# OUTPUT: TREND

# OUTPUT AFTER EACH LINE:

AI = ['T' 'R' 'E' 'N' 'D']
print(AI)  # OUTPUT: ['TREND']

# EXPLANATION:
# This line DOES NOT initialize a list AI with the elements 'T', 'R', 'E', 'N', and 'D'. 
# Since there is no comma separating the elements, 
# they are CONCATENETED together as a single string element in the list.

[print(Py) for Py in AI]  # OUTPUT: TREND

# EXPLANATION:
# This line uses a LIST COMPREHENSION
# to iterate over each element in the list AI 
# and prints each element. 
# As the elements are concatenated together 
# as a single string element 'TREND', 
# the output will be printed as a single word.


####################################################################################################

x = [1, 2, 3]
print(x.clear())

# OUTPUT: None

# EXPLANATION:
x = [1, 2, 3]
# This line initializes a list x 
# with the elements 1, 2, and 3.

print(x.clear())
# This line calls the clear() method on the list x 
# and attempts to print the result. 
# The clear() method removes all elements 
# from the list and returns None, 
# which represents the absence of a value.


####################################################################################################

S = ['Stay', 'Hard']
Y = ['Yes!' for x in S]
print(Y[1])

# OUTPUT: Yes!

# OUTPUT AFTER EACH LINE:

S = ['Stay', 'Hard']
print(S)  # OUTPUT: ['Stay', 'Hard']

Y = ['Yes!' for x in S]
print(Y)  # OUTPUT: ['Yes!', 'Yes!']

print(Y[1])  # OUTPUT: Yes!

# EXPLANATION:
S = ['Stay', 'Hard']
# This line initializes a list S 
# with the elements 'Stay' and 'Hard'.

Y = ['Yes!' for x in S]
# This line uses a list comprehension 
# to iterate over each element in the list S. 
# For each element, the value 'Yes!' 
# is added to the new list Y. 
# Since S has two elements, 'Stay' and 'Hard', 
# the list comprehension will 
# create a new list Y 
# with two elements, 'Yes!' and 'Yes!'.

print(Y[1]) 
# This line prints the second element of the list Y, 
# which is 'Yes!', using index 1. 
# Python uses 0-based indexing, 
# so the second element has an index of 1.


####################################################################################################

for x in {1,2,3,}:
    print(x)

# OUTPUT: 1 2 3


x = [1, 2, 3]
del x[1]
print(x[1])

# OUTPUT: 3


x = [1, 2, 3]
y = [2, 1]
x.extend(y)
print(x[3])

# OUTPUT: 2


if p in apple:
  print('pp')

# OUTPUT: Error


x = [1, 2, 3]
print(x[-1])

# OUTPUT: 3


money = {'j','o','b'}
print(money)

# OUTPUT: Any combination of 'j','o','b'
# {'j','o','b'} ✅
# {'o','b','j'} ✅
# {'b','j','o'} ✅


print(bool(0))
print(bool(None))

# OUTPUT: 
# False 
# False


truth = list((3,2,1))
print(truth[2*(0+1)])

# OUTPUT: 1


x = 4
print(x//=2)

# OUTPUT: invalid syntax


print(bool(()))
print(bool([0]))

# OUTPUT: 
# False
# True


x = 1
x ^= 2
print(x)

# OUTPUT: 3


y = '50'
print(y.zfill(3))

# OUTPUT: 050


x = '{1}{0}'
print(x.format(1, 0))

# OUTPUT: 01


TEA = "GINGER TEA"
print("SUGAR" not in TEA)

# OUTPUT: True


Future = 'HOOMAN AI'
print(Future.replace('HOOMAN', 'AI'))

# OUTPUT: AI AI


PY = 'Ice Cream'
print(PY.split(' ')[1])

# OUTPUT: Cream


GM = 'Love yourself'
print(GM.upper())

# OUTPUT: LOVE YOURSELF


DC = 'PYTHON'
print(DC[4:])

# OUTPUT: ON


DC = int(3.2) 
print(100*DC)

# OUTPUT: 300


print(type(1+2j)

# OUTPUT: <class 'complex'>


Py = b'AT'
print(Py)

# OUTPUT: b'AT'


x = 1j
print(x)

# OUTPUT: 1j


D,E,A,R = 'Py'
print(D+E+A+R)

# OUTPUT: PyPyPyPy


C, O = 'C', 'O'
print(2*(C + O))

# OUTPUT: COCO


one = input()  #1
print(one + one)

# OUTPUT: 11


#print(1) 
print(23)

# OUTPUT: 23


if 10 < 24:
print('Correct') 
print('Me')

# OUTPUT: Error