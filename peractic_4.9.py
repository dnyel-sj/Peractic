# شرط بررسی مثلث بودن
a = eval(input("Add aval vared kn :"))
b = eval(input("Add dovom vared kn :"))
c = eval(input("Add sevom vared kn :"))

p = a  + b + c

if a+b>c and a+c>b and c+b>a :
    print(f"mosals shoma mored taiid ast {p}")
else :
    print("Mosalas nmitone bashe!")   
     
