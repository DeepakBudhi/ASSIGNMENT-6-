a = input("Enter a string with hyphens in it : ")


def hyphen(string):
   string.strip("-")
   if "-" in string :
      s = string.split("-")
      k = []
      for i in s :
          if " " in i :
              d = i.replace(" ","")
              k.append(d)
          elif " " not in i :
              k.append(i)
      k.sort()

      print(k)
      b = ""
      for j in k:
          if j == '':
              continue
          elif j != '' and k.index(j)!=len(k)-1:
              print(j,'-',end = '')
      print(k[-1])
   elif "-" not in string :
       print("Please enter a string which contains hyphens")


hyphen(a)