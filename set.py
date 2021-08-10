#set will avoid duplicates

set = {"laptop","computer","worn","word"}
#print(set)
set2 = {"laptop","computer","charger","keyboard","laptop"}
#print(set2)
"""
set = {} #wrong(dictnory)
set = set()#correct
"""


print("intersection",set.intersection(set2))
print(set.difference(set2))
print(set.union(set2))