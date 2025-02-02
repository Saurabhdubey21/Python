# sets and dictionary
# empty sets
empty_set={1,2,3}
print(empty_set)
# from a list
set_from_list=set({1,2,3})
print(set_from_list)
# set modules
empty_set.add(4)
print(empty_set)
empty_set.remove(4)
print(empty_set)
empty_set.discard(4)
print(empty_set)
removed_set=empty_set.pop()
print(removed_set)
print(empty_set)