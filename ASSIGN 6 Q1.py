a = int(input("Enter a number : "))


def perfect_number(a):
  sum_var = 0
  i = 1
  for i in range(1,a):
    if a % i == 0:
        sum_var = sum_var + i
    else:
        continue
    i = i + 1
  if sum_var == a:
    print("Yes, It's a perfect number ")
  else :
    print("No, Its not a perfect number.")


perfect_number(a)
