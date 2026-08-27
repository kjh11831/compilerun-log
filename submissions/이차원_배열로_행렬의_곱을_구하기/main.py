import sys
v=list(map(int,sys.stdin.read().split()))
a=v[0:4]
b=v[4:8]
print(a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3])
print(a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])