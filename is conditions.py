text="Miruthula"
print("istitle=",text.istitle())#returns true if the string follows the rules of a title(first letter of the string must be capital)

text="    "
print("isspace=",text.isspace())#returns true if all characters in the string are whitespaces

text="2006"
print("isnumeric=",text.isnumeric())#returns true if all characters in the string are numeric

text="miruthula_2006"
print("isidentifier=",text.isidentifier())#returns true if the string is a valid identifier(alphanumeric letters or underscores)

text="miruthula_2006"
print("isprintable=",text.isprintable())#returns true if all characters in the string are printable(allows string not allow escape sequence \n,\t,...)

text="miruthula1009"
print("isalnum=",text.isalnum())#returns true if the string contains only letters and digits

text="miruthula"
print("isalpha=",text.isalpha())#returns true if the string contains only letters
print("isascii=",text.isascii())#returns true if the string contains ascii characters(a-z)

text="400000000"
print("isdecimal=",text.isdecimal())#returns true if the string contains decimal(0-9) 
print("isdigit=",text.isdigit())#returns true if the string contains only digits

