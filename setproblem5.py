# impliment a programe to check if one set is a set is a subset of another
set1 = {1, 2, 3, 4, 5}
set2 = {10,11,12,13}
print(set1.issubset(set2))
# 2nd method
is_subset=set1<=set2
print(is_subset)
# 3rd way
is_subset=all(elem in set1 for elem in set2)
print(is_subset)
# 4th method
is_subset=not(set1-set2)
print(is_subset)
# using filter 
is_subset=set(filter(lambda x:x in set1,set2))
print(is_subset)
# 6thmethod
is_subset=all(map(lambda x:x in set1,set2))
print(is_subset)
# 7th method
is_subset=True
for elem in set1:
    if elem not in set2:
        is_subset=False
        break
    if is_subset:
        print(is_subset)
