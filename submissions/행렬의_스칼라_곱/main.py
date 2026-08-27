import sys
v=list(map(int,sys.stdin.read().split()))
k=v[4]
print(v[0]*k, v[1]*k)
print(v[2]*k, v[3]*k)