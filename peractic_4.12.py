# دریافت عدد از کاربر
num = int(input("Yek add sahih vared kn: "))

# بررسی بخش پذیری بر 5
if num % 5 == 0:
    print(f"{num} Bar 5 bakhsh pazir ast.")
else:
    print(f"{num} Bar 5 bakhsh pazir nist.")

# بررسی بخش پذیری بر 6
if num % 6 == 0:
    print(f"{num} Bar 6 bakhsh pazir ast.")
else:
    print(f"{num} Bar 6 bakhsh pazir nist.")
