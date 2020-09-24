i = int(input("zadej počet(2-20):"))
a = 1

def my_function():
  print("|", " " * (a+2), "|")

if i in range(2,21):
  for a in range(1,i+1):
    print(" /", "=" * a, "\\")
    for y in range(1,a):
      my_function()
    print(" \\", "=" * a, "/","\n")
    a += 1
else:
  print("Zadali jste špatnou hodnotu!")  
