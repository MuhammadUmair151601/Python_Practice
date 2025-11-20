# a normal string is printed as below:
# name = "muhammad umair"
# print(name)

# now if we want to do string slicing:
# nameSlice = name[0:8] 
# it will print the elements from 0 to 7 8 is excluded.
# print(nameSlice)

# negative indexes works as its negative numbering starts as -1 from the last one character:
# slicing with skip value states as
# [0:6:2]
# print 0 to 5 and skip every 2nd value of the string:

# Example:
# sample = "Hello everyone how are you all"
# sampleSkip = sample[0:12:2]
# print(sampleSkip)
# [:8] will print from 0 to 7 string:
# [3:] will print from 3 to end:

# ****************string methods:
# len() shows the length of the string:
# name = "lasdjflksfj"
# print(len(name))
# print(name.endswith("fj"))
# print(name.count("f"))
# print(name.capitalize())
# print(name.find("sdj"))
# print(name.replace("djfl","sldkf"))