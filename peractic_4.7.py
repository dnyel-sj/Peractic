# معادله درجه دوم
import math
a = eval(input("Avalin add vared kn :"))
b = eval(input("Dovomin add vared kn :"))
c = eval(input("Sevomi add vared kn:"))

# فرمول دلتا
delta = (b**2) - (4*a*c)

# شرط های لازم
if delta > 0 :
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"Delta 2 ta rishe dare : {x1} VA {x2}")

elif delta == 0 :
    x = (-b) / (2*a)
    print(f"Delta 1 javab dre : {x}")

else :
    print("Delta hich jabvab ndarad!")
