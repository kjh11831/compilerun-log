import sys
v=list(map(int,sys.stdin.read().split()))
s1=v[0]+v[1]+v[2]
s2=v[3]+v[4]+v[5]
s3=v[6]+v[7]+v[8]
f="학생%d 총점: %d, 평균: %.1f"
print(f % (1, s1, s1/3))
print(f % (2, s2, s2/3))
print(f % (3, s3, s3/3))