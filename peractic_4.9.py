# برنامه مقایسه قیمت دو بسته

# دریافت وزن و قیمت بسته اول
وزن_بسته_1 = float(input("Vzn baste ra vared kn : "))
قیمت_بسته_1 = float(input("Gheymat baste aval vared kn : "))

# دریافت وزن و قیمت بسته دوم
وزن_بسته_2 = float(input("Vazn baste dovom ra vared kn : "))
قیمت_بسته_2 = float(input("Gheymat baste dovom vared kn : "))

# محاسبه قیمت هر کیلوگرم برای هر بسته
قیمت_هر_کیلو_بسته_1 = قیمت_بسته_1 / وزن_بسته_1
قیمت_هر_کیلو_بسته_2 = قیمت_بسته_2 / وزن_بسته_2

# مقایسه قیمت هر کیلوگرم دو بسته
if قیمت_هر_کیلو_بسته_1 < قیمت_هر_کیلو_بسته_2:
    print("Baste aval gheymat behtari dare.")
elif قیمت_هر_کیلو_بسته_1 > قیمت_هر_کیلو_بسته_2:
    print("Baste dovom gheymat behtari dare.")
else:
    print("Gheymat 2 baste teksan ast.")
