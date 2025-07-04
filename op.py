#task-1
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
if x>y and x>z:
  print("x is largest")
elif y>x and y>z :
 print("y is largest")
else:
  print("z is largest")
#task-2
x=float(input("x="))
y=float(input("y="))
z=float(input("z="))
if x<y and x<z:
  print("x's CGPA is the lowest")
elif y<x and y<z :
 print("y's CGPA is the lowest")
else:
  print("z's CGPA is the lowest")
avg=(x+y+z)/3
print(f"Average CGPA= {avg:.2f}")
a= 2
b= 4
c = a | b
d = a & b
e = ~a 
print( c, d, e)
