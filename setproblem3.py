# wap to find the union , intersection, and differrence in three different set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {7, 8, 9, 10, 11}
print(set1)
print(set2)
print(set3)
set4 = set1.union(set2, set3)
set5 = set1.intersection(set2, set3)
set6 = set1.difference(set2, set3)
print("Union of set1, set2, set3: ", set4)
print("Intersection of set1, set2, set3: ", set5)
print("Difference of set1, set2, set3: ", set6)
union_set=set1|set2|set3
intersection_set=set1&set2&set3
difference_set=set1-set2-set3
print("Union of set1, set2, set3: ", union_set)
print("Intersection of set1, set2, set3: ", intersection_set)
print("Difference of set1, set2, set3: ", difference_set)