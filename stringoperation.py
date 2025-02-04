import re
print(re.match("a.b","a.bcd"))
print(re.search("cat","cat is here"))
print(re.findall("\d","A123682375"))
print(re.sub("\s","-","Hello world"))
text="my age is 25 and your age is 35"
print(re.findall("\d+",text))
# .
# \d 
# \w 
# \s 
# *
# +
# ?