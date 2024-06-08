# Calculator Program | by thinhdev

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Division by zero is not allowed"
  else:
    return x / y

print("vui lòng chọn phép tính")
print("1. +")
print("2. -")
print("3. X")
print("4. :")

while True:
  choice = input("Nhập lựa chọn (1/2/3/4): ")

  if choice in ('1', '2', '3', '4'):
    num1 = float(input("nhập số đầu tiên: "))
    num2 = float(input("nhập số thứ hai: "))

    if choice == '1':
      print("kết quả :")
      print(num1, "+", num2, "=", add(num1, num2))
      break

    elif choice == '2':
      print("kết quả :")
      print(num1, "-", num2, "=", subtract(num1, num2))
      break

    elif choice == '3':
      print("kết quả :")
      print(num1, "*", num2, "=", multiply(num1, num2))
      break

    elif choice == '4':
      print("kết quả :")
      print(num1, "/", num2, "=", divide(num1, num2))
      break

  else:
    print("lệnh của bạn bị sai")