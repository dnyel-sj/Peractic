#حل معادله قانون کرامر
a = eval(input("Yek add entekhab kn :"))
b = eval(input("Yek add entekhab kn :"))
c = eval(input("Yek add entekhab kn :"))
d = eval(input("Yek add entekhab kn :"))
e = eval(input("Yek add entekhab kn :"))
f = eval(input("Yek add entekhab kn :"))

if (a*d) - (b*c) > 0 :
    x = ((e*d) - (b*f)) / ((a*d) - (b*c))
    y = ((a*f) - (e*c)) / ((a*d) - (b*c))
    print(f"Meghdar x : {x}")
    print(f"Meghdar y : {y}")

elif (a*d) - (b*c) < 0 :   
    x = ((e*d) - (b*f)) / ((a*d) - (b*c))
    y = ((a*f) - (e*c)) / ((a*d) - (b*c))
    print(f"Meghdar x : {x}")
    print(f"Meghdar y : {y}")
else :
    print("Meghdar mored nazar barabr 0 va tarif nshode ast!")    
