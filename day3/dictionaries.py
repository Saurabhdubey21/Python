# wap to count frequency of charcters in string using a dictionaries
def count_char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            return frequency
print(count_char_frequency("hello"))
text="Hello World"
print(text)
char_count={}
for char in text:
    char_count[char]=char_count.get(char,0)+1
    print("character frequency",char_count)