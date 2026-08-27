import sys
v=list(map(int,sys.stdin.read().split()))
n=v[0]
a=v[1:1+n*n]
ok=all(a[i*n+j]==a[j*n+i] for i in range(n) for j in range(n))
print("대칭" if ok else "비대칭")