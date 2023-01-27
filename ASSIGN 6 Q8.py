a = int(input("Enter number of items in ur list : "))
p = []
for i in range(a):
    b = int(input(f"Enter the element at {i+1}th position : "))
    p.append(b)

s = len(p)


class SumZero:

    def findTriplets(self,m,l):
        found = False
        for i in range(0,l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    if m[i]+m[j]+m[k] == 0:
                        print(m[i] , m[j], m[k])
                        found = True

        if found == False:
            print("Not Found")

a1 = SumZero()
a1.findTriplets(p,s)