# دریافت نمرات از کاربر
نمره_اول = float(input("Nomre dars aval vared kn:"))
نمره_دوم = float(input("Nomre dars dovom vared kn:"))
نمره_سوم = float(input("Nomre dars sevom vared kn:"))

# محاسبه معدل
معدل = (نمره_اول + نمره_دوم + نمره_سوم) / 3

# چاپ معدل
print("Moadle shoma {} ast. ".format(معدل))

# تعیین وضعیت تحصیلی
if معدل >= 17:
    وضعیت_تحصیلی = "Awlii"
elif معدل >= 15:
    وضعیت_تحصیلی = "Khob"
elif معدل >= 12:
    وضعیت_تحصیلی = "Ghabel ghabol"
else:
    وضعیت_تحصیلی = "Mardod"

# چاپ وضعیت تحصیلی
print("Vaziat tahsili shoma {} ast.".format(وضعیت_تحصیلی))
