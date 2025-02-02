from functools import reduce
set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
set3={1,2,3,4,5,6,7}
Union_result=reduce(set.union,[set1,set2,set3])
print("union_result",Union_result)
intersection_result=reduce(set.intersection,[set1,set2,set3])
print("intersection_result",intersection_result)
difference=reduce(set.difference,[set1,set2,set3])
print("difference",difference)
# 4th method using list
set1={1,2,3,4,5}
set2={1,2,3,4,5,6}
set3={1,2,3,4,5,6,7}
intersection_result={x for x in set1 if x in set2 and x in set3}
print("intersection result",intersection_result)