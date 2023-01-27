word = input("Enter a string : ")


def letscheck(a):
  alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  temp = 0
  for i in alphabets :
    if i in a.upper() :
        temp = 1
        continue
    if i not in a.upper() :
        temp = 0
        break

  if temp == 0 :
      print("No,Its not a pangram ")
  if temp ==  1 :
      print("Yes,Its a pangram")


letscheck(word)

