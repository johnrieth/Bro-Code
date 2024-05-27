# slicing is making a substring
# indexing[] or slice()
# [start:stop:step]

name = "Bro Code"

first_name = name[0:3]
last_name = name[4:8]
funky_name = name[0:8:2]
# reverse a string
reversed_name = name[::-1]

# short
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::2]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "https://google.com"
website2 = "https://wikipedia.com"
slicer = slice(8, -4)
print(website2[slicer])
