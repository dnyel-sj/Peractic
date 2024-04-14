# تبدیل نرخ پول از دلار به تومان بر بالعکس
num_1 = eval(input("add mored nazar be dollar vared kn :"))
num_2 = eval(input("add mored nazar be toman vared kn :"))

if num_2 ==0 :
  x = eval(input("add ra be dollar vared kn :"))
  print(f" {x}, hast {x*num_1} toman")

elif num_2 == 1 :
  y = eval(input("add ra be toman vared kn :"))  
  print(f" {y}, hast {y/num_1} dollars")

else :
  print("add mored nazar dar mahdode mojod nist!")
    
