text="miruthula"
print("title=",text.title())#converts the first character of each word to upper case

text="my favourite colour is blue"
print("zfill=",text.zfill(40))#fills the string with zeroes until it is 40 characters long

text="mIRUTHULA"
print("capitalize=",text.capitalize())#converts the first letter of a string into upper case
print("casefold=",text.casefold())#converts uppercase letters to lowercase

text="miruthula"
print("center=",text.center(50))#align a string to the center
print("count=",text.count("miruthula"))#returns the number of times of character in string
print("encode=",text.encode())#encodes the string
print("endswith=",text.endswith("a"))#returns true if the string ends with the specified value
print("startswith=",text.startswith("m"))#returns true if the string starts with the specified value
print("find=",text.find("miruthula"))#searching a substring within a string,returns -1 if not found and 0 if found
print("index=",text.index("u"))#returns the position of the specified value(first occurence)
print("rindex=",text.rindex("u"))#returns the position of the specified value(last occurence)

text="          miruthula  "
print("strip=",text.strip())#returns a trimmed version of the string(removes the unwanted space in start and at end)
print("rstrip=",text.rstrip())#returns a right trimmed version of the string
text="          benz "
x=text.lstrip()#returns a left trimmed version of the string
print("of all cars",x,"is my favourite")
