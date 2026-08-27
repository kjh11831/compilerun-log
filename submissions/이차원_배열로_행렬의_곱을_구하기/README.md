# 이차원 배열로 행렬의 곱을 구하기

**난이도:** ★★★
**문제 링크:** https://compilerun.vercel.app/problems/0ecd4670-62f5-497f-8646-2c0b2da68697

## 문제 지문

2×2 행렬 A, B를 각 줄에 4개씩 입력받아 행렬 곱 A×B를 2줄로 출력하세요. 곱의 각 원소는 C[i][j] = Σ A[i][k]×B[k][j] 입니다.

[입력] 첫째 줄: A의 4원소 / 둘째 줄: B의 4원소
[출력]
(곱 행렬 1행)
(곱 행렬 2행)

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
a=v[0:4]
b=v[4:8]
print(a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3])
print(a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int a[2][2], b[2][2], c[2][2] = {{0}};
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) scanf("%d", &a[i][j]);
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) scanf("%d", &b[i][j]);
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                c[i][j] += a[i][k] * b[k][j];
    for (int i = 0; i < 2; i++) {
        printf("%d %d\n", c[i][0], c[i][1]);
    }
    return 0;
}
```

## 해설

행렬 곱은 A의 i행과 B의 j열의 내적입니다. [[1,2],[3,4]]×[[5,6],[7,8]] = [[19,22],[43,50]]

_해결일: 2026-08-27_