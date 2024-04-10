#تولید سه عدد صحیح تک رقمی تصادفی و از کاربر خواسته میشود حاصل جمه سه عدد حساب کند
import random

# تولید 3 عدد تصادفی تک رقمی
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)

# جمع 3 عدد
total = num1 + num2 + num3

# دریافت حدس کاربر
guess = int(input("jame 3 add chand mishavad? {}, {}, {},: ".format(num1, num2, num3)))

# بررسی صحت حدس کاربر
if guess == total:
    print("Awlii! dorost hads zdi.")
else:
    print("Motasefane eshtebah hads zadidi! {} ".format(total))
