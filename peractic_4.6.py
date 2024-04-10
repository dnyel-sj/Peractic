# دریافت قد و وزن از کاربر
قد = float(input("Ghad khod ra be metr vared konid : "))
وزن = float(input("Vazn khod ra be kilo vared konid : "))

# محاسبه BMI
bmi = وزن / (قد ** 2)

# چاپ BMI
print("Shakhes BMI shoma in add {} Hast.".format(bmi))

# تعیین وضعیت سلامتی
if bmi < 18.5:
    وضعیت_سلامتی = "Kambod vazn"
elif bmi < 25:
    وضعیت_سلامتی = "Vazn normal"
elif bmi < 30:
    وضعیت_سلامتی = "Ezafe vazn"
else:
    وضعیت_سلامتی = "Chaghi"

# چاپ وضعیت سلامتی
print("Vaziat salamati shoma dar halet {} Hast".format(وضعیت_سلامتی))
