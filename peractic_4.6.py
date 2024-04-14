# دریافت قد و وزن از کاربر
Ghad = float(input("Ghad khod ra be metr vared konid : "))
vazn = float(input("Vazn khod ra be kilo vared konid : "))

# محاسبه BMI
bmi = vazn / (Ghad** 2)

# چاپ BMI
print("Shakhes BMI shoma in add {} Hast.".format(bmi))

# تعیین وضعیت سلامتی
if bmi < 18.5:
    vaziat_salamati = "Kambod vazn"
elif bmi < 25:
    vaziat_salamati = "Vazn normal"
elif bmi < 30:
    vaziat_salamati = "Ezafe vazn"
else:
    vaziat_salamati = "Chaghi"

# چاپ وضعیت سلامتی
print("Vaziat salamati shoma dar halet {} Hast".format(vaziat_salamati))
