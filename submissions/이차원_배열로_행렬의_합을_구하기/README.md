# 이차원 배열로 행렬의 합을 구하기

**난이도:** ★★
**문제 링크:** https://compilerun.vercel.app/problems/5b16ae18-55b9-4bb0-a287-cdacc2ace15e

## 문제 지문

2×2 행렬 두 개를 각 줄에 4개씩 두 줄로 입력받아, 두 행렬의 합을 2줄로 출력하세요.

[입력] 첫째 줄: 행렬A의 4원소 / 둘째 줄: 행렬B의 4원소
[출력]
(합 행렬 1행: 두 값 공백 구분)
(합 행렬 2행)

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
print(v[0]+v[4], v[1]+v[5])
print(v[2]+v[6], v[3]+v[7])
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int a[2][2], b[2][2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) scanf("%d", &a[i][j]);
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) scanf("%d", &b[i][j]);
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            if (j) printf(" ");
            printf("%d", a[i][j] + b[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

## 해설

C[i][j] = A[i][j] + B[i][j] — 행렬 덧셈은 원소별 덧셈입니다.

_해결일: 2026-08-27_