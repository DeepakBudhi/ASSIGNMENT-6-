a = input("Enter a series of brackets : ")


class Brackets:
    def __int__(self,a):
        self.a = a
    for i in range(len(a)):
        if a[i] == "(" and a[i+1]!=")":
            ans = "It is an invalid series of brackets "
            break
        elif a[i] == "{" and a[i+1]!="}":
            ans = "It is an invalid series of brackets "
            break
        elif a[i] == "[" and a[i+1]!="]":
            ans = "It is an invalid series of brackets "
            break
        elif i == len(a)-1 :
            ans = "It is a correct series of brackets."


B1 = Brackets()
print(B1.ans)