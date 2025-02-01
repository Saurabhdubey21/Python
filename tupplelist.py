# # wap to demonstrate the difference between shallow and deep copies of list contain tuples
import copy
original_list =[(1, 2),(3, 4),[5,6],(7,8),(11,12),(13,15),[17,19],[19,21],[21,23]]
shallow_copy=copy.copy(original_list)
deep_copy=copy.deepcopy(original_list)
original_list[2][0]=99
print("original list:",original_list)
print("shallow copy:",shallow_copy)
print("deep copy:",deep_copy)