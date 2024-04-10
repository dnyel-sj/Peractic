# دریافت اعداد از کاربر
اعداد = list(map(int, input("3 add be sorat jodagane vared konid : ").split()))

# مرتب سازی اعداد با استفاده از روش افزایشی
for i in range(len(اعداد)):
    for j in range(i + 1, len(اعداد)):
        if اعداد[i] > اعداد[j]:
            اعداد[i], اعداد[j] = اعداد[j], اعداد[i]

# چاپ اعداد مرتب شده
print("add haye vared shode be sorat nozoli be in sorat ast :{}".format(اعداد))
