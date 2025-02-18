# 1. Using get(key, default) 
student = {"name": "Saurabh", "age": 18} 
print(student.get("name")) 
print(student.get("grade", "Not available"))
# 2. Using keys() 
keys = student.keys() 
print(keys) 
# 3. Using values() 
values = student.values() 
print(values)
# 4. Using items() 
items = student.items() 
print(items)
# 5. Using update(other_dict) 
extra_info = {"grade": "A", "city": "Motihari"} 
student.update(extra_info) 
print(student)
# 6. Using pop(key) 
age = student.pop("age") 
print(age)
print(student) 
# 7. Using popitem() 
last_item = student.popitem() 
print(last_item)
print(student) 
# 8. Using clear() 
student.clear() 
print(student)