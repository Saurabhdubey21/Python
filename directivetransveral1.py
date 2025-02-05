def check_age(age):
    if age < 18:
        raise ValueError('age must be older than 18')
    print("age is valid")
try:
    check_age(16)
except ValueError as e:
    print("Exception:",e)