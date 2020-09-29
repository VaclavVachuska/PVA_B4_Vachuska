i = input("zadej text: ")

a = i.split(" ")

for slovo in a:
  print("/", "=" * len(slovo), "\\", end="") 
print("")
for slovo in a:
  print("|", slovo, "|", end="")
print("")
for slovo in a:
  print("\\", "=" * len(slovo), "/", end="") 
print("")
