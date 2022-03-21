introString = input("Enter any string: ")

cc = 0
wc = 1

for m in introString:
    cc = cc + 1
    if(m == " "):
        wc = wc + 1

print("Number of Characters: ")
print(cc)
print("Number of Words: ")
print(wc)