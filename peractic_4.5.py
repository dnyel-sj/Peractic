# برنامه محاسبه روز هفته آینده

# دریافت تاریخ امروز به عنوان عدد صحیح
today = int(input("Tarish emroz be add vared kn :"))

# دریافت تعداد روزهای سپری شده از تاریخ امروز
days_passed = int(input("Roz separi shode az tarikh emroz vard kn :"))

# محاسبه روز هفته امروز
day_of_week = today % 7

# محاسبه روز هفته فردا
tomorrow_day_of_week = (day_of_week + days_passed) % 7

# تبدیل عدد روز هفته به نام روز
names_of_days = ["shanbe", "yekshanbe", "doshanbe", "seshanbe ", "chaharshanbe", "panjshanbe", "jome"]
tomorrow_name_of_day = names_of_days[tomorrow_day_of_week]

# چاپ خروجی
print("Emroz :{}".format(names_of_days[day_of_week]))
print("Tarikh {} roz bad hast: {} ".format(days_passed, tomorrow_name_of_day))
