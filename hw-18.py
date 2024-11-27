import array as arr
a=arr.array('i',[1200,1500,1100,1700,1600,1800,1300,1900,1750,1600,1400,1500])
b=list(reversed(a))
c=arr.array('i',[1600,1700])
a.extend(c)
print(a[5])
print(b)
print(a)


import array as arr
a=arr.array('i',[90,78,89,70,95,56,79,80,92,88])
a[3]=77
print(a)
print("Highest score = ",a[4])
print("Least score = ",a[5])

import array as arr
a=arr.array('d',[10.99, 5.49, 20.00, 7.95, 12.75])
l=a.tolist()
print(sum(a))
a.remove(5.49)
print(a)
a.append(17.87)
print(a)





