import sys
v=list(map(int,sys.stdin.read().split()))
n=v[0]
m=v[1]
a=v[2:2+n*m]
b=v[2+n*m:2+2*n*m]
d=[a[i]-b[i] for i in range(n*m)]
print("\n".join(" ".join(map(str,d[i*m:(i+1)*m])) for i in range(n)))