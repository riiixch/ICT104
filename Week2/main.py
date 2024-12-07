num = 2
multi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
author = "65064435 สมภพ เอี่ยมสมบีติ"

for x in multi:
  print("{} * {} = {}".format(num, x, num * x))
  if len(multi) == x:
    print(author)
    break
