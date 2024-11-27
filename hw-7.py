cosmetic_brands={"Lakme":["foundation","matte finish lipstick","eyeliner","face wash"],
                 "maybelline":["pot kajal","liner","lipliner"],
                 "loreal":["kajal","eyeshadow","lipsticks"],
                 "mac":["moisturiser","primer","eyeliner"],
                 "bobbibrown":["concealer","eyeshadow","mascara"]}
brand=input()
if brand in cosmetic_brands:
    print(cosmetic_brands[brand])
            
else:
    print("Not Available")


num1=int(input())
num2=int(input())
operation=int(input())
print("1.Add  2.Sub  3.Mul  4.Div  5.Exp")
match operation:
    case 1:
        Add=num1+num2
        print(Add)
    case 2:
        Sub=num1-num2
        print(Sub)
    case 3:
        Mul=num1*num2
        print(Mul)
    case 4:
        Div=num1/num2
        print(Div)
    case 5:
        Exp=num1**num2
        print(Exp)
    case _:
        print("Invalid Operation")
    




        
