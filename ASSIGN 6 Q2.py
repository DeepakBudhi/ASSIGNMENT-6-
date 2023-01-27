s = input("Enter a string : ")
a = s.replace(" ","")
b = len(a)
c = ""
for i in range(1,b+1):
    c = c + a[len(a)-i]

if a == c:
    print("Yes , It is a palindrome string.")
else:
    print("No ,It is not a palindrome string ")