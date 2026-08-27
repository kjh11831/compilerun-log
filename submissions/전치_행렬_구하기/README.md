# 전치 행렬 구하기

**난이도:** ★★
**문제 링크:** https://compilerun.vercel.app/problems/9cecf3cf-5225-40a9-bfc2-ec9155235743

## 문제 지문

2×3 행렬의 원소 6개를 한 줄로 입력받아(행 우선), 행과 열을 뒤바꾼 전치 행렬(3×2)을 3줄로 출력하세요.

[입력] 정수 6개 (공백 구분, 행 우선)
[출력]
(전치 행렬 — 3줄, 각 줄 2개 공백 구분)

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
print(v[0], v[3])
print(v[1], v[4])
print(v[2], v[5])
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int a[2][3];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 3; j++)
            scanf("%d", &a[i][j]);
    for (int j = 0; j < 3; j++)
        printf("%d %d\n", a[0][j], a[1][j]);
    return 0;
}
```

## 해설

T[j][i] = A[i][j] — 인덱스를 뒤바꾸면 전치가 됩니다.

_해결일: 2026-08-27_