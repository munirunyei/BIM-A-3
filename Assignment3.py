import math
n= int(input ("number of points:"))

while n < 3:
      n= int(input("the number is not valid:"))

i=0
x=[]
y=[]
while i < n:
    i= i+1
    x.append(int(input(f"input x{i}: ")))
    y.append(int(input(f"input y{i}: ")))


j = 0
A = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
XT = 0
YT = 0
IXT = 0
IYT = 0


while j < (n-1):

    A = 1 / 2 * (x [j + 1] + x[j] ) * (y [j + 1] - y[j]) + A
    
    Sx = -1/6 * (x [j + 1] - x[j]) * (y [j + 1] **2 + y[j] * y [j + 1] + y[j] **2) + Sx

    Sy = 1/6 * (y [j + 1] - y[j]) * (x [j + 1] **2 + x[j] * x [j + 1] + x[j]**2) + Sy

    Ix = -1/12 * (x [j + 1] - x[j]) * (y [j + 1] **3 + y [j + 1] **2 * y [j + 1] * y[j]**2 + y[j]**3) + Ix

    Iy = 1/12 * (y [j + 1] - y[j]) * (x [j + 1] **3 + x [j + 1] **2 * x [j + 1] * x[j]**2 + x[j]**3) + Iy

    Ixy = -1/24 * (y [j + 1] - y[j]) * ((y [j + 1]) * (3 * x[j + 1] **2 + 2*x[j + 1] * x[j] + x[j]**2) + y[j]* (3 * x[j]**2 + 2 * x [j + 1] * x[j]) + x[j]**2) + Ixy

    j = j+1


XT = Sy / A

YT = Sx / A

IXT = Ix - YT**2 * A

IYT = Iy - XT**2 * A
    

print("The area of the polygon", A)
print("Static moment of cross section", Sx )
print("Static moment of cross section", Sy )
print("Cross section moment of inertia", Ix )
print("Cross section moment of inertia", Iy )
print("Cross section moment of inertia", Ixy )
print("Xt", XT )
print("Yt", YT )
print("IXT", IXT )
print("IYT", IYT )