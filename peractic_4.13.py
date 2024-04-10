# برنامه ای برای محاسبه مالیات برای اظهارکنندگان مجرد

# وارد کردن وضعیت تأهل
status = input("Vaziat rabete khod ra vared knid (singel): ")

# وارد کردن درآمد مشمول مالیات
income = float(input("Daramad shoma ke tax be an talogh migirad ra vared kn : "))

# محاسبه مالیات
tax = 0

# محاسبه مالیات برای اظهارکنندگان مجرد
if status == "singel":
    if income <= 9875:
        tax = income * 0.1
    elif income <= 40125:
        tax = 987.50 + (income - 9875) * 0.12
    elif income <= 85525:
        tax = 4617.50 + (income - 40125) * 0.22
    else:
        tax = 14605.50 + (income - 85525) * 0.24

# چاپ نتیجه
print("Mablagh tax shoma :", tax)
