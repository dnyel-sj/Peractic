import random

def main():
  # دو عدد تصادفی بین 1 تا 100 تولید می کنیم
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)

  # سوال را به کاربر نمایش می دهیم
  print(f"Quiz {num1} * {num2} = ?")

  # جواب کاربر را دریافت می کنیم
  answer = int(input())

  # بررسی می کنیم که جواب کاربر درست است یا نه
  if answer == num1 * num2:
    print("Awlii, javabet dorost bod.")
  else:
     print(f"Akh, javab dorost barabar {num1 * num2} ast.")

if __name__ == "__main__":
  main()
