#PROGRAM FOR TUPLE ELEMENTS
l=() or tuple()
l1=(1,2,3)
l2=tuple((4,5,6,"JAVA","C programming",3.14))
print(l1,"\n",l2,"\n",l)


# string to tuple
str='python programming'
num=[1,2,3,4,5]
print(tuple(num))
print(tuple(str))

#program fo adding or deleting
#Tuples are immutable: once created, you cannot delete or reassign elements inside them.
del l[3]
del l[2] # tuple not support deletinon
print(l)
l[3]="html" # tuple is unchangeable
print(l)