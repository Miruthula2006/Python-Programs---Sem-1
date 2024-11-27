num=int(input())
if num%3==0 and num%5==0:
    print("Divisible by both")
elif num%3==0:
    print("Divisible by 3")
elif num%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible")

fi=int(input())
si=int(input())
ti=int(input())
bc=fi+si+ti
if bc>400:
    tax=int((6.7/100)*bc)
    tip=int((10/100)*(tax+bc))
print(bc)
print(tax)
print(tip)
print(bc+tax+tip)

w=float(input())
h=float(input())
bmi=w/h**2
print(bmi)
if bmi<16:
    print("Severe Thinness")
elif 16<=bmi<17:
    print("Moderate Thinness")
elif 17<=bmi<18.5:
    print("Mild Thinness")
elif 18.5<=bmi<25:
    print("Normal")
elif 25<=bmi<30:
    print("Overweight")
elif 30<=bmi<35:
    print("Obese Class I")
elif 35<=bmi<40:
    print("Obese Class II")
else:
    print("Obese Class III")
