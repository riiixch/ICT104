def fac(n):
  if n == 0:
    return 1
  else:
    return n * fac(n - 1) 

def fibonacci(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fibonacci(n - 2) + fibonacci(n - 1)

t = 0
def hanoi(n, a, b, c):
  global t
  if(n > 0):
    hanoi(n-1, a, c, b)
    t += 1
    print("%d. ย้ายจานที่ %d จาก %s ไป %s"%(t, n, a, c))
    hanoi(n-1, b, a, c)
  else:
      return

print("ข้อที่ 1 :")
n_fac = 6
print("%d! = %d" % (n_fac, fac(n_fac)))

print("")
print("ข้อที่ 2 :")
n_fibonacci_1 = 7
print("Fibonacci sequence at position ", end = "")
print("%d is %d" % (n_fibonacci_1 , fibonacci(n_fibonacci_1)))

n_fibonacci_2 = 12
print("Fibonacci sequence at position ", end = "")
print("%d is %d" % (n_fibonacci_2 , fibonacci(n_fibonacci_2)))

print("")
print("ข้อที่ 3 :")
hanoi(4, 'A', 'B', 'C')

print("")
print("65064435 สมภพ เอี่ยมสมบีติ")