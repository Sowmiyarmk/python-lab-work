a={1,2,3,4}
b={1,2,5,6,7}
print("UNION :",a|b or a.union(b))
print("INTERSECTION:",a&b or a.difference(b))
print("CARAT OR SYMMENTRIC DIFFERENCE:",a^b or a.symmetric_difference(b))
print("DIFFERENCE OF A-B:",a-b or a.difference(b))
print("DIFFERENCE OF B-A :",b-a or b.symmetric_difference(a))