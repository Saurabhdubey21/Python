x = 10 
def outer_function():
   y = 20
   def inner_function():
    nonlocal y
    y += 10
print(f"Nonlocal y: {y}")
# inner_function()
print(f"Global x: {x}")
outer_function()