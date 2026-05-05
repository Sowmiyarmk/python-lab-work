lang=["java",'c','cpp','sql','SQL']
l1=sorted(lang)
print("THE SORTED LIST L1 :",l1)
print("THE SORTED LIST L :",sorted(lang))
print("THE ORIGINAL LIST L :",lang)
print("the sort list l returning NONE :",lang.sort())
print("THE SORTED LIST L2 is descending order using sorted is :",sorted(lang,reverse=True))
print("THE original updated  LIST using sort is :",lang)
lang.sort(reverse=True)
print("THE UPDATED SORTED LIST (descending order) using sort is :",lang)




