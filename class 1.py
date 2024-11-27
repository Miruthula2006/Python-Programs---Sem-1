text="I could drive all day,drive safely"
x=text.partition("drive")#returns a tuple where the string is parted into three parts(first occurence)
y=text.rpartition("drive")#splits the string for the last occurence
print(x)
print(y)

text="I like cars"
x=text.replace("cars","automatic cars")#returns a string where a specified value is replaced with a specified value
print(x)

text="Hello Drivers!"
mytrans=str.maketrans("l","L")#returns a translation table to be used in translations
print(text.translate(mytrans))
