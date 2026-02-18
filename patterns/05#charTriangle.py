# In Python, you can't directly add a number to a string like in some other languages
# Using ord() and chr()
n = 4

for i in range(n):
    ch = chr(ord("A") + i)
    for j in range(i+1):
        print(ch, end = " ")
    print()
